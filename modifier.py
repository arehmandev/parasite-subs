from datetime import datetime, timedelta

sub_data_file = open("parasite_subs.srt")
sub_data = sub_data_file.read()
sub_data_file.close()

timestamp_format = "%H:%M:%S,%f"
time_modifier_s = -2
time_modifier_ms = 0

new_file_name = "parasite_time_modified_subs.srt"


def modify_stamp(timestamp_input, position=2):

    parsed_timestamp = datetime.strptime(
        timestamp_input+"000", timestamp_format)
    parsed_timestamp = parsed_timestamp + \
        timedelta(seconds=time_modifier_s, milliseconds=time_modifier_ms)

    corrected_timestamp = parsed_timestamp.strftime(
        timestamp_format)[:-3]
    return corrected_timestamp


def main():
    new_data = []

    for line in sub_data.split("\n\n"):

        if len(line) < 4:
            continue

        current_timestamp_list = line.split("\n")[1]
        left_timestamp = current_timestamp_list.split(
            " --> ")[0]
        right_timestamp = current_timestamp_list.split(
            " --> ")[1]

        final_new_stamp = "{} --> {}".format(
            modify_stamp(left_timestamp),
            modify_stamp(right_timestamp)
        )

        final_line = line.split("\n")
        final_line[1] = final_new_stamp
        final_line_string = "\n".join(final_line)

        new_data.append(final_line_string)

    new_file_data = "\n\n".join(new_data)
    new_file = open(new_file_name, "w")
    new_file.write(new_file_data)
    new_file.close()


main()
