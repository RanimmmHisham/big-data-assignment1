mkdir -p service-result/

CONTAINER_NAME=bd-a1-container

docker cp $CONTAINER_NAME:/home/doc-bd-a1/res_dpre.csv service-result/
docker cp $CONTAINER_NAME:/home/doc-bd-a1/eda-in-1.txt service-result/
docker cp $CONTAINER_NAME:/home/doc-bd-a1/eda-in-2.txt service-result/
docker cp $CONTAINER_NAME:/home/doc-bd-a1/eda-in-3.txt service-result/
docker cp $CONTAINER_NAME:/home/doc-bd-a1/vis.png service-result/
docker cp $CONTAINER_NAME:/home/doc-bd-a1/k.txt service-result/

docker stop $CONTAINER_NAME