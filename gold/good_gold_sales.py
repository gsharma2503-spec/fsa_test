from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as spark_sum

def main():
    spark = SparkSession.builder.appName("gold").getOrCreate()

    df = spark.read.format("delta").load("/mnt/bronze/sales")

    result = df.groupBy("customer_id").agg(spark_sum(col("amount")).alias("total"))

    result.write.format("delta").mode("overwrite").save("/mnt/gold/sales")

if __name__ == "__main__":
    main()
