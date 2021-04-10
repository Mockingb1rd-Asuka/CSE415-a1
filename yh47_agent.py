'''yh47_agent.
CSE 415, Winter 2020, Assignment 1
Jerry Hong
'''

import chatbot

if __name__ == "__main__":
    you_me = {'I': 'you', 'me': 'you', 'you': 'me', 'am': 'are',
              'mine': 'yours', 'my': 'your', 'yours': 'mine', 'your': 'my'}
    self_introduction = "Hi! My name is Nanase. I graduated from Waseda University, Mathematics " \
                        "department. I studied data science. Such as samlping, building data model, and predicting." \
                        " You can just call me Nana. I'm not good at talking. Sorry about that."

    nanase_rules = [
        (r"[^\.!?]*you[\s]like[\s]me[^\.!?]*[\.!?]*",
         ["Thank you...I think I like you too."]),
        (r"[^\.!?]*(N|nana)[^\.!?]*[\.!?]*",
         ["Did you just call me Nana? I'm so happy.",
          "You just said Nana? Please say it again."]),
        (r"(W|w)hat[^\.!?]*me[^\.!?]*math[^\.!?]*[\.!?]*",
         ["I studied in data science in Waseda University during grad student period.",
          "I'm a data scientist now.",
          "Data science is my major field."]),
        (r"[^\.!?]*(B|bot)[^\.!?]*[\.!?]*",
         ["Please don't call me bot, I'm a human.",
          "My name is Nanase, and you can call me Nana."]),
        (r"[^\.!?]*normal distribution[\.!?]*",
         ["In probability theory, a normal (or Gaussian or Gauss or Laplace–Gauss) "
          "distribution is a type of continuous probability distribution for a "
          "real-valued random variable."
          "The parameter mu is the mean or expectation of "
          "the distribution (and also its median and mode); "
          "and sigma is its standard deviation. "
          "The variance of the distribution is sigma^2. "
          "A random variable with a Gaussian distribution is said to be normally distributed "
          "and is called a normal deviate."]),
        (r"[^\.!?]*me[^\.!?]*like[^\.!?]*[\.!?]*",
         ["I like pigeons, painting, staying alone"]),
        (r"[^\.!?]*you[^\.!?]*like (.*)[\.!?]*",
         ["Please tell me more about $1$.",
          "I'm also interested in $1$."]),
        (r"((What)|(How))[^\.!?]*work[^\.!?]*[\.!?]*",
         ["The main things I do are collecting data, building up data models, "
          "getting conclusion and doing predictions"]),
        (r"((Hi)|(Hello))[\.!?]*",
         ["Hello! My name is Nanase, a data scientist. How can I help you?"]),
        (r"", ["I'm listening.", "I see...", "Please go on.", "Sorry, I don't quite understand."])
    ]

    Nanase_Bot = chatbot.chatbot(nanase_rules, you_me, "Nanase", self_introduction)
    Nanase_Bot.chat()
