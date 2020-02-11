
sub_data_file = open("parasite_subs.srt")
sub_data = sub_data_file.read()
sub_data_file.close()

time_modifier = -2
new_file = "parasite_time_modified_subs.srt"


def modify_stamp(timestamp_list, position, time_modifier):
    timestamp_s = str(
        int(timestamp_list[position].split(",")[0]) + time_modifier)

    timestamp_ms = timestamp_list[position].split(",")[1]

    if int(timestamp_s) < 10:
        timestamp_s = "0" + str(timestamp_s)

    timestamp_list[position] = timestamp_s + "," + timestamp_ms


def main(new_file):
    new_data = []

    for line in sub_data.split("\n\n"):

        if len(line) < 4:
            continue

        current_timestamp_list = line.split("\n")[1].split(":")

        modify_stamp(current_timestamp_list, 2, time_modifier)
        modify_stamp(current_timestamp_list, 4, time_modifier)

        final_new_stamp = ":".join(current_timestamp_list)
        final_line = line.split("\n")
        final_line[1] = final_new_stamp
        final_line_string = "\n".join(final_line)

        new_data.append(final_line_string)

    new_file_data = "\n\n".join(new_data)
    new_file = open(new_file, "w")
    new_file.write(new_file_data)
    new_file.close()


main(new_file)
