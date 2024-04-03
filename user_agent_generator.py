from bs4 import BeautifulSoup
import httpx

def get_user_agents():
    url = "https://www.useragentlist.net/"
    request = httpx.get(url)
    user_agents = []
    soup = BeautifulSoup(request.text, "html.parser")
    for user_agent in soup.select("pre.wp-block-code"):
        user_agents.append(user_agent.text.strip())
    return user_agents
