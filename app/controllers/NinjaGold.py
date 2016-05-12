
from system.core.controller import *
import datetime, random

class NinjaGold(Controller):
    def __init__(self, action):
        super(NinjaGold, self).__init__(action)

        self.load_model('NinjaGoldModel')
        self.db = self._app.db

    def index(self):
 
        if "score" not in session:
            session["score"] = 0
        if "text" not in session:
            session["text"] = []
        return self.load_view('index.html')

    def process_gold(self):
        now = datetime.datetime.now()
        tformat = "%a %b %d, %Y %H:%M:%S"
        newTime = now.strftime(tformat)
        if request.form["action"] == "farm":
            farmgold = random.randint(10,20)
            session["score"] += farmgold
            session["text"].insert(0,"Earned " + str(farmgold) + " golds from the farm! " + newTime)
        elif request.form["action"] == "cave":
            cavegold = random.randint(5,10)
            session["score"] += cavegold
            session["text"].insert(0,"Earned " + str(cavegold) + " golds from the cave! " + newTime)
        elif request.form["action"] == "house":
            housegold = random.randint(2,5)
            session["score"] += housegold
            session["text"].insert(0,"Earned " + str(housegold) + " golds from the farm! " + newTime)
        elif request.form["action"] == "casino":
            housegold = random.randint(0,50)
            chance = random.randint(0,1)
            if chance == 0:
                session["score"] += housegold
                session["text"].insert(0,"Won " + str(housegold) + " golds from the Casino! " + newTime)
            else:
                session["score"] -= housegold
                session["text"].insert(0,"Lost " + str(housegold) + " golds from the Casino! " + newTime)
        return redirect('/')

    def reset(self):
        del session['score']
        del session['text']
        return redirect('/')