FROM apache/zeppelin:0.9.0

USER root

RUN mkdir -p /datasets/dataset=yellow_tripdata/year=2013
RUN curl https://s3-eu-west-1.amazonaws.com/615535196854-datalab/datasets/dataset=yellow_tripdata/year=2013/yellow_tripdata_2013-01.csv -o /datasets/dataset=yellow_tripdata/year=2013/yellow_tripdata_2013-01.csv

RUN mkdir -p /datasets/dataset=nyc-borough-boundaries/
RUN curl https://s3-eu-west-1.amazonaws.com/615535196854-datalab/datasets/dataset=nyc-borough-boundaries/nyc-borough-boundaries-polygon.geojson -o /datasets/dataset=nyc-borough-boundaries/nyc-borough-boundaries-polygon.geojson

COPY ch08-geotime-2.0.0-jar-with-dependencies.jar /opt/zeppelin/interpreter/spark/dep/ch08-geotime-2.0.0-jar-with-dependencies.jar
