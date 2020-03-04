# nlg.py
import random
import datetime
from py4j_server import launch_py4j_server
from py4j.java_gateway import java_import

gateway = launch_py4j_server()

# Import the SimpleNLG classes
java_import(gateway.jvm, "simplenlg.features.*")
java_import(gateway.jvm, "simplenlg.realiser.*")

# Define aliases so that we don't have to use the gateway.jvm prefix.
NPPhraseSpec = gateway.jvm.NPPhraseSpec
PPPhraseSpec = gateway.jvm.PPPhraseSpec
SPhraseSpec = gateway.jvm.SPhraseSpec
InterrogativeType = gateway.jvm.InterrogativeType
Realiser = gateway.jvm.Realiser
TextSpec = gateway.jvm.TextSpec
Tense = gateway.jvm.Tense
Form = gateway.jvm.Form


class NLG(object):
    """
    Used to generate natural language. Most of these sections are hard coded. However, some use simpleNLG which is
    used to string together verbs and nouns.
    """
    def __init__(self, user_name=None):
        self.user_name = user_name

        # make random more random by seeding with time
        random.seed(datetime.datetime.now())

    def acknowledge(self):

        user_name = self.user_name
        if user_name is None:
            user_name = ""

        simple_acknoledgement = [
            "Yes?",
            "What can I do for you?",
            "How can I help?"
        ]

        personal_acknowledgement = [
            "How can I help you today, %s" % user_name,
            "How can I help you, %s" % user_name,
            "What can I do for you, %s" % user_name,
            "Hi %s, what can I do for you?" % user_name,
            "Hey %s, what can I do for you?" % user_name
        ]

        choice = 0
        if self.user_name is not None:
            choice = random.randint(0, 2)
        else:
            choice = random.randint(0,1)

        ret_phrase = ""

        if choice == 0:
            ret_phrase = random.choice(simple_acknoledgement)
        elif choice == 1:
            date = datetime.datetime.now()
            ret_phrase = "Good %s. What can I do for you?" % self.time_of_day(date)
        else:
            ret_phrase = random.choice(personal_acknowledgement)

        return ret_phrase

    def searching(self):
        searching_phrases = [
            "I'll see what I can find"
        ]

        return random.choice(searching_phrases)

    def snow_white(self):

        phrases = [
            "You are",
            "You",
            "You are, of course"
        ]

        return random.choice(phrases)

    def user_status(self, type='positive', attribute=None):

        ret_phrase = ""

        positive_complements = [
            "good",
            "nice",
            "great",
            "perfect",
            "Beautiful"
        ]

        negative_complements = [
            "bad",
            "terrible"
        ]

        moderate_complements = [
            "alright",
            "okay"
        ]

        complement_choice = positive_complements
        if type == 'negative':
            complement_choice = negative_complements
        elif type == 'moderate':
            complement_choice = moderate_complements

        if attribute is None:
            ret_phrase = "You look %s" % random.choice(complement_choice)
        else:
            ret_phrase = self.generate('none', {'subject': "Your %s" % attribute, 'verb': 'look %s' % random.choice(complement_choice)}, "present")

        return ret_phrase

    def personal_status(self, status_type=None):
        positive_status=[
            "I'm doing well",
            "Great, thanks for asking",
            "I'm doing great"
        ]

        negative_status = [
            "I'm not doing well",
            "I'm feeling terrible",
            "I'm not doing well today",
            "I could be much better"
        ]

        moderate_status = [
            "I'm doing alright",
            "I'm okay",
            "I could be better",
            "I'm alright"
        ]

        if status_type == 'negative':
            return random.choice(negative_status)
        elif status_type == 'moderate':
            return random.choice(moderate_status)

        return random.choice(positive_status)
    def article_interest(self, article_titles):
        ret_phrase = None

        if random.randint(0,2) == 0: # 1 in 3 chance the bot will express interest in a random article
            if article_titles is not None:
                article = random.choice(article_titles)
                article = article.rsplit('-', 1)[0]
                ret_phrase = "%s sounds particularly interesting" % article

        return ret_phrase

    def insult(self):
        return "That's not very nice. Talk to me again when you have fixed your attitude"


    def appreciation(self):
        phrases = [
            "No problem!",
            "Any time",
            "You are welcome",
            "You're welcome",
            "Sure, no problem",
            "Of course",
            "Don't mention it",
            "Don't worry about it"
        ]

        return random.choice(phrases)

    def holiday(self, holiday_name):
        phrases = [
            "",
            "Looks like the next holiday is ",
            "The next important day is "
        ]

        return "%s%s" % (random.choice(phrases), holiday_name)

    def meaning_of_life(self):
        phrases = [
            "42",
            "The meaning of life, the universe, and everything else is 42"
        ]

        return random.choice(phrases)

    def name(self):
        return self.user_name

    def time_of_day(self, date, with_adjective=False):
        ret_phrase = ""
        if date.hour < 10:
            ret_phrase = "morning"
            if with_adjective:
                ret_phrase = "%s %s" % ("this", ret_phrase)
        elif (date.hour >= 10) and (date.hour < 18):
            ret_phrase = "afternoon"
            if with_adjective:
                ret_phrase = "%s %s" % ("this", ret_phrase)
        elif date.hour >= 18:
            ret_phrase = "evening"
            if with_adjective:
                ret_phrase = "%s %s" % ("this", ret_phrase)

        return ret_phrase

    def generate(self, utter_type, keywords, tense=None):
        """
        Input: a type of inquiry to create and a dictionary of keywords.
        Types of inquiries include 'what', 'who', 'where', 'why', 'how',
        and 'yes/no' questions. Alternatively, 'none' can be specified to
        generate a declarative statement.

        The dictionary is essentially divided into three core parts: the
        subject, the verb, and the object. Modifiers can be specified to these
        parts (adverbs, adjectives, etc). Additionally, an optional
        prepositional phrase can be specified.

        Example:

        nlg = NaturalLanguageGenerator(logging.getLogger())
        words = {'subject': 'you',
                 'verb': 'prefer',
                 'object': 'recipes',
                 'preposition': 'that contains',
                 'objmodifiers': ['Thai'],
                 'prepmodifiers': ['potatoes', 'celery', 'carrots'],
                 'adverbs': ['confidently'],
        }

        nlg.generate('yes_no', words)
        u'Do you confidently prefer Thai recipes that contains potatoes, celery and carrots?'
        nlg.generate('how', words)
        u'How do you confidently prefer Thai recipes that contains potatoes, celery and carrots?'
        """
        utterance = SPhraseSpec()
        subject = NPPhraseSpec(keywords['subject'])
        target = None
        if 'object' in keywords:
            target = NPPhraseSpec(keywords['object'])
        preposition = PPPhraseSpec()

        if 'preposition' in keywords:
            preposition.setPreposition(keywords['preposition'])

        if 'prepmodifiers' in keywords:
            for modifier in keywords['prepmodifiers']:
                preposition.addComplement(modifier)

        if 'submodifiers' in keywords:
            for modifier in keywords['submodifiers']:
                subject.addModifier(modifier)

        if 'objmodifiers' in keywords:
            for modifier in keywords['objmodifiers']:
                target.addModifier(modifier)

        if utter_type.lower() == 'yes_no':
            utterance.setInterrogative(InterrogativeType.YES_NO)
        elif utter_type.lower() == 'how':
            utterance.setInterrogative(InterrogativeType.HOW)
        elif utter_type.lower() == 'what':
            utterance.setInterrogative(InterrogativeType.WHAT)
        elif utter_type.lower() == 'where':
            utterance.setInterrogative(InterrogativeType.WHERE)
        elif utter_type.lower() == 'who':
            utterance.setInterrogative(InterrogativeType.WHO)
        elif utter_type.lower() == 'why':
            utterance.setInterrogative(InterrogativeType.WHY)

        if target is not None:
            target.addModifier(preposition)
        utterance.setSubject(subject)
        utterance.setVerb(keywords['verb'])
        if 'adverbs' in keywords:
            for modifier in keywords['adverbs']:
                utterance.addModifier(modifier)
        if target is not None:
            utterance.addComplement(target)

        if tense.lower() == 'future':
            utterance.setTense(Tense.FUTURE)
        elif tense.lower() == 'past':
            utterance.setTense(Tense.PAST)

        realiser = Realiser()
        output = realiser.realiseDocument(utterance).strip()
        return output
