[![Fetch Search Engine Continuous Integration](https://github.com/sofarikasid/Fetch_Reward_Search/actions/workflows/CI_main.yml/badge.svg)](https://github.com/sofarikasid/Fetch_Reward_Search/actions/workflows/CI_main.yml)
[![Deploy to huggingface](https://github.com/sofarikasid/Fetch_Reward_Search/actions/workflows/Deploy.yml/badge.svg)](https://github.com/sofarikasid/Fetch_Reward_Search/actions/workflows/Deploy.yml)

# Custom Enterprise Search Engine 
This project aims to develop an intelligent search tool that empowers users to retrieve
 relevant offers using natural language input. Users will be able to input prompts based on categories,
 brands, and retailers and receive a list of offers that match their query, along with a similarity score. By
 meeting these criteria, users can efficiently perform contextual information searches, simplifying the
 process of discovering appealing offers based on their preferred categories, brands, and retailers. The
 creation of this search engine encompasses essential steps such as data preparation, feature engineering,
 embedding, vector space database, and automation through Continuous Integration and Continuous
 Deployment (CI/CD) practices. All of these processes are facilitated using software design principles
 and Machine Learning Operations (MLOps) tools and methodologies.

 ### How to Run:
 ```diff
clone repo
$ python -m venv .venv
$ source .venv/bin/activate
$ make install
$ python app.py
```
### Hosted Hugging Face Link
 ```diff
https://huggingface.co/spaces/sofarikasid/Fetch_Reward_Search
```
