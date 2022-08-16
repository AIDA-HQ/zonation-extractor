import tabula
import pathlib

class Scraper:
    def scrape(self, input_file, output_format, output_file):
        """Scrape the PDF file and save the output to a file."""

        # Use current path if no output_file is given
        if output_file == "":
            output_file = str(pathlib.Path(__file__).parent.resolve()) + "/output_file"

        # Generate output path name
        output_path = output_file + "." + output_format

        # Let tabula-py do the magic
        tabula.convert_into(
            input_file,
            output_path,
            output_format,
            pages="all",
        )

        # Remove all non-numerical characters from the output file
        with open(output_path, "r") as f:
            lines = f.readlines()
            lines = [line for line in lines if line[0].isdigit()]
            with open(output_path, "w") as f:
                f.writelines(lines)

if __name__ == "__main__":
    scraper = Scraper()

    # Ask user for input values from cmd line
    input_file = input("Enter the path of the PDF file: ")
    output_format = input("Enter the output format (csv or json): ")
    output_file = input("Enter the name of the output file: ")

    scraper.scrape(input_file, output_format, output_file)