import subprocess
from pyspark.sql import SparkSession

DB_PASSWORD = "SuperSecretPassword123"

def main():
    spark = SparkSession.builder.getOrCreate()

    subprocess.call("ls -ltr /mnt", shell=True)

    print("password:", DB_PASSWORD)

if __name__ == "__main__":
    main()
