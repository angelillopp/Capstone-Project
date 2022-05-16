# Capstone-Project

Main files and folders:
* **Capstone**: Folder that contains all files used.
  * **app.py**: Flask app main file.
  * **Dockerfile**: File to assemble the docker image.
  * **functions.py**: External functions used for training and predicting as well as for processing data.
  * **logs**: Contains all training logs.
  * **models**: Contains all trained models for prediction.
  * **Report.ipynb**: Notebook with EDA and model trainings and comparisions. (Part 1 & 2).
  * **run-tests.py**: Script for running all tests.
  * **templates**: Flask app templates.
  * **unittest**: Folder containing all unittest files (model, api and logs).

## Build the Docker image and run it
```bash
    ~$ cd Capstone
    ~$ docker build -t aavail-app .
```
Check that the image is there.
```bash
    ~$ docker image ls
```
Run the container
```bash
docker run -p 4000:8080 aavail-app
```
## Test the running app
Go to [http://0.0.0.0:4000/](http://0.0.0.0:4000/) to ensure the app is running.

For training: [http://0.0.0.0:4000/train](http://0.0.0.0:4000/train)

For predicting using the model: [http://0.0.0.0:4000/predict](http://0.0.0.0:4000/predict)
