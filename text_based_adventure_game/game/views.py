from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def intro(request):
    return render(request, 'intro.html')


def choose_path(request):
    return render(request, 'choose_path.html')


def path_mountain(request):
    data_object = {
        "status": -1,
        "text": ""
    }
    return render(request, 'path_mountain.html', data_object)


def path_mountain_par(request, pk):
    data_object = {
        "status": -1,
        "text": "",
        "lesson": ''
    }
    if pk == 1:
        data_object["text"] = "Ziac kept fighting with all the " \
               "skill he had, when all of a sudden he " \
               "slips and falls all the way down to the ground. " \
               "Ziac is critically injured and " \
               "will not be able to continue the search."
        data_object["lesson"] = "(wrong choice, you have failed)"
    elif pk == 2:
        data_object["text"] = "Ziac gives up on fighting and lets the eagle carry him away. The eagle keeps flying and flying until " \
               "he reaches his nest in the middle of the mountains. Ziac notices that nobody is there in that nest " \
               "except the eagles babies. “The whole situation does not make sense” said Ziac, and it really did not " \
               "why would there be a piece of cloth from my sister on the eagles claws if she’s not here. started " \
               "thinking and remember that his sister is afraid of many things and if she would have a chance she " \
               "would escape from it as soon as he got a thought about that he notices a strange hole in the eagles, " \
               "which looked like it was dug up. Is it possible that Sophie escaped from the eagles nest? Without " \
               "hesitation Ziac plans on escaping through the same hole when the eagle goes to sleep. After some time " \
               "the eagle goes to sleep as the sun went down and the moon got up. Ziac makes a move and attempts on " \
               "escaping and continuing his search for his sister. as Ziad started moving the eagle woke up right " \
               "away she looked at the Ziac in his eyes and started moving towards him. Ziac got terrified and " \
               "quickly threw himself in that hole not knowing what is waiting for him outside it. As soon as Ziac " \
               "fell through the hole he realized it was a big mistake since he was falling into abyss. All he did " \
               "was closed his eyes and prepared to die. "
        data_object["lesson"] = "(wrong choice, you have failed)"

    data_object["status"] = pk
    print(data_object)
    return render(request, 'path_mountain.html', data_object)


def path_slow_river(request):
    data_object = {
        "status": -1,
        "text": ""
    }
    return render(request, 'path_slow_river.html', data_object)


def path_slow_river_par(request, pk):
    data_object = {
        "status": -1,
        "text": "",
        "lesson": ''
    }
    if pk == 1:
        data_object["text"] = "Ziac has parked the canoe along side the river and started walking towards the house. " \
                              "The house was rather strange and creepy and there is a chance he might get kidnapped " \
                              "and never be able to find his sister again."
        data_object["lesson"] = "There is still time to go back, what choice " \
                              "do you think Ziac should make? "

    elif pk == 2 or pk == 3:
        data_object["text"] = "Ziac starts walking back to the canoe and continues his search along the river. After " \
                              "some time has passed, Ziac notices that the river is moving faster and faster. Just as " \
                              "he realized what is waiting for him he reaches the waterfall and has no time to react. " \
                              "Ziac falls down the waterfall and due to his lack of swimming skills he drowns. "
        data_object["lesson"] = "LESSON: no risks, no results. "

    elif pk == 4:
        data_object["text"] = "Ziac continues walking towards the house in hopes that he could find his sister or any " \
                              "sign of her there. Ziac Approaches the main door and knocks on it. an old lady " \
                              "answered and asked what does he want. Ziac told the old lady about the search for his " \
                              "sister and about everything he has been through while finding his sister. The old lady " \
                              "smiled and opened the door completely through which his sister was seen laying in the " \
                              "bed next to the fire pit. Ziac was at that moment the happiest man alive. He dashed " \
                              "towards her and hugged her with all the love he was gathering for her all these " \
                              "year’s. The old lady explained how she saved her from the eagle that was trying to " \
                              "capture her close by her house. Ziac’s biggest wish became true but another problem " \
                              "arises. Ziac remembers their grand grandpas words when they said that ones you come in " \
                              "the forest you never come out, and so it was true. Ziac and Sophie lived at the old " \
                              "lady’s house happily ever after. "
        data_object["lesson"] = "You did it, you found your sister."

    data_object["status"] = pk
    return render(request, 'path_slow_river.html', data_object)


def about_game(request):
    data_object = {
        "text": ''
                'This is a mini game where you will be in the role of the main character '
                'Zaic and you need to find your sister Sophie. Enjoy the short story, meet the main characters and '
                'experience this exciting adventure with them. '
    }
    return render(request, 'about_game.html', data_object)