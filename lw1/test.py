from argparse import ArgumentParser
from subprocess import check_output
from math import ceil


def parse_command_line_arguments():
    parser = ArgumentParser()
    parser.add_argument("target_file_name", type=str)
    parser.add_argument("test_cases_file_name", type=str)

    args = parser.parse_args()
    return args.target_file_name, args.test_cases_file_name


def get_formatted_comparison_result(result, line_index, args):
    return f'{line_index}[{3 * line_index - 2}]: {"Success" if result else "Failed"} {args}'


def main():
    target_file_name, test_cases_file_name = parse_command_line_arguments()
    with open(test_cases_file_name, "r") as test_cases_file:
        lines = test_cases_file.read().splitlines()
        command_line_arguments = list(map(lambda arguments: arguments.split(" "), lines[0::3]))
        expected_outputs = lines[1::3]

        line_indexes = [index for index in range(1, 1 + ceil((len(lines)) / 3))]
        for args, expected_output, line_index in zip(command_line_arguments, expected_outputs, line_indexes):
            output = check_output(["python", target_file_name] + args).strip()
            print(get_formatted_comparison_result(output.decode("utf-8") == expected_output, line_index, args))


if __name__ == "__main__":
    main()
