# ...existing code...
import csv
import os
from typing import List, Optional, Tuple
def compute_stats(values: List[float]) -> Optional[Tuple[float, float, float]]:
    if not values:
        return None
    return (sum(values) / len(values), min(values), max(values))
def read_numeric_column(path: str, column: Optional[str] = None, delimiter: str = ",") -> List[float]:
    nums: List[float] = []
    with open(path, newline="", encoding="utf-8") as f:
        # If user provided a column name, use DictReader; otherwise use reader and treat column as index (int)
        if column is not None and not column.isdigit():
            reader = csv.DictReader(f, delimiter=delimiter)
            if column not in reader.fieldnames:
                raise ValueError(f"Column '{column}' not found in CSV headers: {reader.fieldnames}")
            for row in reader:
                val = row.get(column, "").strip()
                if val:
                    try:
                        nums.append(float(val))
                    except ValueError:
                        pass  # ignore non-numeric cells
        else:
            # column is index or None -> use numeric index (default 0 if None)
            reader = csv.reader(f, delimiter=delimiter)
            idx = int(column) if column and column.isdigit() else 0
            for row in reader:
                if idx < len(row):
                    val = row[idx].strip()
                    if val:
                        try:
                            nums.append(float(val))
                        except ValueError:
                            pass
    return nums
# ...existing code...

def create_sample_csv(path: str) -> None:
    rows = [
        ["id", "value", "label"],
        ["1", "10.5", "a"],
        ["2", "7.2", "b"],
        ["3", "15.0", "c"],
        ["4", "3.8", "d"],
        ["5", "", "e"],
        ["6", "not_a_number", "f"],
    ]
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
def run_auto():
    sample_path = os.path.join(os.getcwd(), "sample_data.csv")
    create_sample_csv(sample_path)
    print(f"Sample CSV created at: {sample_path}\n")

    # show CSV contents
    print("Sample CSV contents:")
    with open(sample_path, newline="", encoding="utf-8") as f:
        for row in csv.reader(f):
            print(row)
    print()
    # compute stats for 'value' column
    try:
        values = read_numeric_column(sample_path, column="value", delimiter=",")
        stats = compute_stats(values)
        if stats is None:
            print("No numeric values found in the 'value' column.")
        else:
            mean, minimum, maximum = stats
            print("Statistics for column 'value':")
            print(f"Count: {len(values)}")
            print(f"Mean: {mean}")
            print(f"Min: {minimum}")
            print(f"Max: {maximum}")
    except Exception as e:
        print("Error:", e)
# Auto-run without asking for input
run_auto()
# ...existing code...




