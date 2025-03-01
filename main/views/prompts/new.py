from main.models import Prompt


EMOJIS = [
    "😀", "😁", "😂", "🤣", "😃", "😄", "😅", "😆", "😉", "😊", "😋", "😎", "😍", "😘", "😗", "😙", "😚",  
    "🙂", "🤗", "🤩", "🤔", "🤨", "😐", "😑", "😶", "🙄", "😏", "😣", "😥", "😮", "🤐", "😯", "😪", "😫",  
    "😴", "😌", "😛", "😜", "😝", "🤤", "😒", "😓", "😔", "😕", "🙃", "🤑", "😲", "☹️", "🙁", "😖", "😞",  
    "😟", "😤", "😢", "😭", "😦", "😧", "😨", "😩", "🤯", "😬", "😰", "😱", "🥵", "🥶", "😳", "🤪", "😵",  
    "😠", "😡", "🤬", "😷", "🤒", "🤕", "🤢", "🤮", "🤧", "😇", "🥳", "🥺", "🤠", "🤡", "🤥", "🤫", "🤭",  
    "🧐", "🤓", "😈", "👿", "💀", "☠️", "👽", "🤖", "🎃", "😺", "😸", "😹", "😻", "😼", "😽", "🙀", "😿",  
    "😾", "🙈", "🙉", "🙊", "🐵", "🐒", "🦍", "🐶", "🐕", "🐩", "🐺", "🦊", "🦝", "🐱", "🐈", "🦁", "🐯",  
    "🐅", "🐆", "🐴", "🐎", "🦄", "🦓", "🦌", "🐮", "🐂", "🐃", "🐄", "🐷", "🐖", "🐗", "🐽", "🐏", "🐑",  
    "🐐", "🐪", "🐫", "🦙", "🦒", "🐘", "🦏", "🦛", "🐭", "🐁", "🐀", "🐹", "🐰", "🐇", "🐿️", "🦔", "🦇",  
    "🐻", "🐨", "🐼", "🦘", "🦡", "🦃", "🐔", "🐓", "🐣", "🐤", "🐥", "🐦", "🐧", "🕊️", "🦅", "🦆", "🦢",  
    "🦉", "🐸", "🐊", "🐢", "🦎", "🐍", "🐲", "🐉", "🦕", "🦖", "🐳", "🐋", "🐬", "🐟", "🐠", "🐡", "🦈",  
    "🐙", "🐚", "🦀", "🦞", "🦐", "🦑", "🐌", "🦋", "🐛", "🐜", "🐝", "🐞", "🦗", "🕷️", "🕸️", "🦂", "🌵",  
    "🎄", "🌲", "🌳", "🌴", "🌱", "🌿", "☘️", "🍀", "🎍", "🎋", "🍃", "🍂", "🍁", "🍄", "🌾", "💐", "🌷",  
    "🌹", "🥀", "🌺", "🌸", "🌼", "🌻", "🌞", "🌝", "🌛", "🌜", "🌚", "🌕", "🌖", "🌗", "🌘", "🌑", "🌒",  
    "🌓", "🌔", "🌙", "🌎", "🌍", "🌏", "🪐", "⭐", "🌟", "✨", "⚡", "🔥", "💥", "☄️", "🌈", "☀️", "🌤️",  
    "⛅", "🌥️", "🌦️", "☁️", "🌧️", "⛈️", "🌩️", "🌨️", "❄️", "☃️", "⛄", "🌬️", "💨", "🌪️", "🌫️", "🌊",  
    "💧", "💦", "☔", "☂️", "🍏", "🍎", "🍐", "🍊", "🍋", "🍌", "🍉", "🍇", "🍓", "🍈", "🍒", "🍑", "🥭",  
    "🍍", "🥥", "🥝", "🍅", "🥑", "🥒", "🥬", "🥦", "🌽", "🥕", "🧄", "🧅", "🥔", "🍠", "🥐", "🥖", "🥨",  
    "🥯", "🍞", "🧀", "🥚", "🍳", "🥞", "🧇", "🥓", "🥩", "🍗", "🍖", "🌭", "🍔", "🍟", "🍕", "🥪", "🥙",  
    "🌮", "🌯", "🥗", "🥘", "🥫", "🍝", "🍜", "🍲", "🍛", "🍣", "🍤", "🍚", "🍙", "🍘", "🥟", "🍢", "🍡",  
    "🍧", "🍨", "🍦", "🥧", "🍰", "🎂", "🧁", "🍮", "🍭", "🍬", "🍫", "🍿", "🍩", "🍪", "🌰", "🥜", "🥛",  
    "🍼", "☕", "🍵", "🍶", "🍾", "🍷", "🍸", "🍹", "🍺", "🍻", "🥂", "🥃", "🥤", "🥢", "🍽️", "🍴", "🥄",  
    "🚗", "🚕", "🚙", "🚌", "🚎", "🏎️", "🚓", "🚑", "🚒", "🚐", "🚚", "🚛", "🚜", "✈️", "🛫", "🛬", "🛩️",  
    "🚀", "🛸", "🚁", "🚂", "🚊", "🚆", "🚄", "🚅", "🚈", "🚇", "🚉", "🚏", "🛣️", "🛤️", "🗺️", "🏔️", "⛰️",  
    "🌋", "🏕️", "🏖️", "🏜️", "🏝️", "🏞️", "🏟️", "🏛️", "🏗️", "🏘️", "🏚️", "🏠", "🏡", "🏢", "🏣", "🏤",  
    "🏥", "🏦", "🏨", "🏩", "💒", "⛪", "🕌", "🛕", "🕍", "⛩️", "🗼", "🗽", "⛲", "🎡", "🎢", "🎠"
]


# when GET, return a promt_message consisting of two random emojis
# on POST, create a Prompt object based on the message and the current user
def prompt_new(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        if message:
            Prompt.objects.create(user=request.user, message=message)
            return redirect('prompt')
    
    prompt_message = "Create a story using the following emojis: " + random.choice(EMOJIS) + random.choice(EMOJIS)
    return render(request, 'prompts/prompt.html', {'prompt_message': prompt_message})

