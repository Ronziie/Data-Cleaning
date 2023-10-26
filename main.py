import csv

def write_batch_to_csv(batch, batch_number):
    filename = f"recipe-batch-sheet-{batch_number}.csv"
    with open(filename, 'w', newline='') as batch_csv:
        csv_writer = csv.writer(batch_csv, delimiter='\t')
        csv_writer.writerows(batch)

def process_csv(input_filename, recipes_per_csv):
    with open(input_filename, 'r') as input_csv:
        csv_reader = csv.reader(input_csv, delimiter='\t')
        current_batch = []
        batch_number = 1
        blank_count = 0
        
        for row in csv_reader:
            if not row:
                blank_count += 1
                if blank_count % recipes_per_csv == 0:
                    write_batch_to_csv(current_batch, batch_number)
                    batch_number += 1
                    current_batch = []
            else:
                blank_count = 0
                current_batch.append(row)

        if current_batch:
            write_batch_to_csv(current_batch, batch_number)

if __name__ == "__main__":
    input_csv_filename = "input.csv"  # Replace with your input CSV filename
    recipes_per_csv = 100  # Number of recipes per CSV
    process_csv(input_csv_filename, recipes_per_csv)
