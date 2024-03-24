# mispLLMsGalaxy
A galaxy of opensource LLMs

## Description

The goal is to create a JSON file that contains every opensource LLMs and their specificities such as their score or their architecture with the MISP galaxy format.
I could not be more precise about the descriptions of the models being given the size of the files and the number of different models. That’s why, my description includes the different tags used to qualify the models.
I had some issues regarding the scraping of the site https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard since all the data is loaded dynamically and I have not succeeded in getting access to the api to make my own requests. That is why I use the scrape-open-llm-leaderboard tool.

## How to use:

1. Clone the project:

    ```
    git clone https://github.com/MacAaronGlacey/mispLLMsGalaxy.git
    ```

2. Go to the project directory:

    ```
    cd mispLLMsGalaxy
    ```

3. Use this project in order get a JSON file that contains every public model from https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard:

    [scrape-open-llm-leaderboard](https://github.com/Weyaxi/scrape-open-llm-leaderboard)

    Do not forget to specify the JSON format for good to get a JSON file and not a csv file. 

4. Put the JSON into the mispLLMsGalaxy directory and execute `getTags.py` to get the tags related to every models.

    ```
    python getTags.py
    ```

    It will create a new JSON named "updated_models.json" which contains the Tags related to each model, if the page is not available, it will delete the model from the file.

5. Use `clustering.py` to get the cluster format.

    ```
    python clustering.py
    ```

    Congratulations, if everything was done correctly, you should find the cluster in the directory "clusters". At each use the cluster file is replaced.


