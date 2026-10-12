from pathlib import Path

def save_to_csv(df, output_path: Path):
    """ Save DataFrame to CSV file """

    output_file = Path(output_path)

    output_file.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_file, index=False)

    print(f"Data saved to {output_file}")