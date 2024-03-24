## mispLLMsGalaxy

A MISP-compatible galaxy of opensource LLMs.

## Description :

The goal is to create a JSON file that contains every opensource LLMs and their specificities such as their score or their architecture with the MISP galaxy format.
I could not be more precise about the descriptions of the models being given the size of the files and the large number of  models. That is why, my description fields includes the different tags used to qualify the models.
I had some issues regarding the scraping of the site https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard since all the data is loaded dynamically and I have not succeeded in getting access to the api to make my own requests. That is why I use the scrape-open-llm-leaderboard tool.

## Sources :

open_llm_leaderboard : https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard

Additional information on model evaluation parameters :

[HellaSwag](https://arxiv.org/abs/1905.07830)
[MMLU](https://arxiv.org/abs/2009.03300)
[TruthfulQA](https://arxiv.org/abs/2109.07958)
[Winogrande](https://arxiv.org/abs/1907.10641)
[GSM8k](https://arxiv.org/abs/2110.14168)
 
## How to use :

1. Clone the project :

    ```
    git clone https://github.com/MacAaronGlacey/mispLLMsGalaxy.git
    ```

2. Go to the project directory :

    ```
    cd mispLLMsGalaxy
    ```

3. Use this project in order get a JSON file that contains every public model from the open_llm_leaderboard :

    [scrape-open-llm-leaderboard](https://github.com/Weyaxi/scrape-open-llm-leaderboard)

    Do not forget to specify the JSON format for good to get a JSON file and not a csv file. 

4. Put the JSON into the mispLLMsGalaxy directory and execute `getTags.py` to get the tags related to every models :

    ```
    python getTags.py
    ```

    It will create a new JSON named "updated_models.json" using the "open-llm-leaderboard.json" you created earlier. The goal is to go to each model webpage, get the tags related to each LLM and add them to our JSON file. The tags are used as a description for the models since the description files are way too heavy.

5. Use `clustering.py` to get the cluster format :

    ```
     clustering.py
    ```

    Congratulations, if everything was done correctly, you should find the cluster in the directory "clusters". At each use the cluster file is replaced.


