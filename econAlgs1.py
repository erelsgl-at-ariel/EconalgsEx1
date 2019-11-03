"""
Defines an Agent class, that represents an agent in a cake-cutting algorithm.
AUTHOR: Erel Segal-Halevi
SINCE:  2019-10
"""

"""
this is a submission for question 7. Not too long, so here is a cake to divide:
           ~                  ~
     *                   *                *       *
                  *               *
  ~       *                *         ~    *
              *       ~        *              *   ~
                  )         (         )              *
    *    ~     ) (_)   (   (_)   )   (_) (  *
           *  (_) # ) (_) ) # ( (_) ( # (_)       *
              _#.-#(_)-#-(_)#(_)-#-(_)#-.#_
  *         .' #  # #  #  # # #  #  # #  # `.   ~     *
           :   #    #  #  #   #  #  #    #   :
    ~      :.       #     #   #     #       .:      *
        *  | `-.__                     __.-' | *
           |      `````""""""""""""`````      |         *
     *     |         | ||\ |~)|~)\ /         |
           |         |~||~\|~ |~  |          |       ~
   ~   *   |                                 | *
           |      |~)||~)~|~| ||~\|\ \ /     |         *
   *    _.-|      |~)||~\ | |~|| /|~\ |      |-._
      .'   '.      ~            ~           .'   `.  *
      :      `-.__                     __.-'      :
       `.         `````""""""""""""`````         .'
         `-.._                             _..-'
              `````""""-----------""""`````

submittor info:
name: Guy Wolf
I.D: 212055966
"""

from typing import List
import statistics

class Agent:
    def eval(self, x:float)->float:
        """
        :param    x: a positive number representing a location on the cake.
        :return:  v: the value of the piece [0,x] for the agent.
        """
        pass

    def mark(self, v:float)->float:
        """
        :param    v: a positive number representing a value of a piece.
        :return:  x: a number such that the value of [0,x] equals v.
        """
        pass

def cutAndChoose(a:Agent, b:Agent):
    """
    :param a, b: two agents.
    :return:  prints a fair division of the cake [0,1].
    """
    normA = a.eval(1)
    normB = b.eval(1)
    midCut = a.mark(0.5*normA)
    if(b.eval(midCut)/normB < 0.5):
        print("Agent a receives [", str(0), ",", str(midCut), "].", end = " ")
        print("Agent b receives [", str(midCut), ",", str(1), "].")
    else:
        print("Agent a receives [", str(midCut), ",", str(1), "].", end = " ")
        print("Agent b receives [", str(0), ",", str(midCut), "].")

def algEvenPaz(agents:List[Agent]):
    """
    :param agents: a list of agents.
    :return:  prints a fair division of the cake [0,1].
    """
    division = [None for _ in range(len(agents))]
    def evenPazMemoization(agentIdxs, start, end):
        lenAgents = len(agentIdxs)
        assert lenAgents>0, "no agents at assigned area of " + str(start) + ", " + str(end)
        if lenAgents == 1:
            division[agentIdxs[0]] = (start, end)
        else:
            if lenAgents % 2 == 0:
                targetMark = 0.5
            else:
                targetMark = (lenAgents-1)/(2*lenAgents)
            cuts = []
            for i in agentIdxs:
                agent = agents[i]
                normalizer = agent.eval(end) - agent.eval(start)
                trueMark = targetMark*normalizer
                cut = agent.mark(agent.eval(start) + trueMark)
                cuts.append(cut)
            median = statistics.median(cuts)
            leftAgents = []
            rightAgents = []
            for i in range(lenAgents):
                if cuts[i] < median:
                    leftAgents.append(agentIdxs[i])
                else:
                    rightAgents.append(agentIdxs[i])
            evenPazMemoization(leftAgents, start, median)
            evenPazMemoization(rightAgents, median, end)
            
    agentIdxs = range(len(agents))
    evenPazMemoization(agentIdxs,0,1)
    for i in range(len(agents)):
        cut = division[i]
        print("Agent " , str(i), " receives [", str(cut[0]), ",", str(cut[1]), "].", end = " ")


class TestAgent(Agent):
    """test class for a really basic agent to see if algorithms work.
    The agent assigns all value in the line to a single point, given in the constructor."""
    def __init__(self, point):
        self.point = point

    def eval(self, x:float)->float:
        """
        :param    x: a positive number representing a location on the cake.
        :return:  v: the value of the piece [0,x] for the agent.
        """
        if(x >= self.point):
            return self.point
        return 0

    def mark(self, v:float)->float:
        """
        :param    v: a positive number representing a value of a piece.
        :return:  x: a number such that the value of [0,x] equals v.
        """
        #note that due to the nature of this agent the division can't accuratly be done to be exactly equal to v, and thus a shortcut was taken
        if v > 0:
            return self.point
        return 0
