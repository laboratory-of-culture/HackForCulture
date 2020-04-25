
# AI-based recommendation system for Events Terminal project

[![Getting Started](misc/hack.png)](https://hatathon.houseofeurope.org.ua/)

This code was developed in frame of online ideathon 24–26 April 2020 as potential AI-feature for existent [Events Terminal](https://eventsterminal.com/) resourse

  - Here we did PoC (Proof of Concept) how deeply personalize content
  - We tried to find undestand user interests and preferences through twitter account (in future version also Facebook and Instagram will be available)
  - Magic is under Natural Language Processing


# User Case

At the moment you do not login on Events Terminal, hence content is not personalized.
In future this will be possible using OAuth (as you usually login to other web-resourses with you existent Facebook or Linkedin account, for e.g. to pass some funny tests).

After that ( of course policy agreement for storing and protecting your personal data  will be confirmed by you) AI-algorimths will explore you page (posts, shares, likes, check-ins etc) and detect your interests. Based on that data only more relevant event will apper visiting Events Terminal.

### USAGE
Specifying twitter username (for e.g. `elonmusk` for Elon Musk or `realdonaldtrump` for Donal Trump) in `app.py`


```sh
(env) atuzhykov@PC:~/HackForCulture$ python app.py elonmusk
User elonmusk keywords: starlink teslas human spaceflight launch new update former ceo dogecoin meme necromancer
Seems like event A System for Financial Inclusion fits this twitter account. Please visit https://eventsterminal.com/event/a-system-for-financial-inclusion
```

or ...

```sh
(env) atuzhykov@PC:~/HackForCulture$ python app.py realdonaldtrump
User realdonaldtrump keywords: fake news lamestream media sick coronavirus cdc ventilators hoax united states america 45th president
Seems like event How to Crack the Product Manager Interview by Gayle McDowell fits this twitter account. Please visit https://eventsterminal.com/event/how-to-crack-the-product-manager-interview-by-gayle-mcdowell


```