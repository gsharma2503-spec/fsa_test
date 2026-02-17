from pyspark.sql import SparkSession

def main():
    spark = SparkSession.builder.getOrCreate()

    df = spark.read.format("delta").load("/mnt/bronze/customers")

    rows = df.collect()

    for r in rows:
        print(r)

    df2 = df.repartition(1)
    df.join(df2).write.format("delta").mode("overwrite").save("/mnt/silver/customers")

if __name__ == "__main__":
    main()
