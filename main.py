import webbrowser
from googletrans import Translator


def open_browser(request):
    webbrowser.open(request)


def request_browser(request, browser, language):
    translator = Translator()
    if browser == "g":
        request = request.replace(" ", "+")
        if language == "ru":
            translation_request = translator.translate(request, dest='ru')
        elif language == "en":
            translation_request = translator.translate(request, dest='en')
        open_browser(f"https://www.google.ru/search?q={translation_request.text}")
    elif browser == "y":
        request = request.replace(" ", "+")
        if language == "ru":
            translation_request = translator.translate(request, dest='ru')
        elif language == "en":
            translation_request = translator.translate(request, dest='en')
        open_browser(f"https://yandex.ru/search/?text={translation_request.text}")


def main():
    request = input("введите запрос: ")
    browsers = ["google", "yandex"]
    languages = ["ru", "en"]
    char_name_browser = []
    rq = ""
    for browser in browsers:
        if browser[0] not in char_name_browser:
            rq += f" {browser} - {browser[0]}"
            char_name_browser.append(browser[0])
        else:
            rq += f" {browser} - {browser[0] + browser[1]}"
            char_name_browser.append(browser[0] + browser[1])
    browser = input(f"выберите браузер по первой букве:{rq}: ")
    language = input(f"русский - {languages[0]} английский - {languages[1]}: ")
    flab_lang = True
    if language not in languages:
        flab_lang = False
    if browser in char_name_browser and flab_lang:
        request_browser(request, browser, language)
    else:
        flag = True
        while flag:
            browser = input(f"выберите браузер по первой букве:{rq}: ")
            language = input(f"русский - {languages[0]} английский - {languages[1]}: ")
            flab_lang = True
            if language not in languages:
                flab_lang = False
            if browser in char_name_browser and flab_lang:
                request_browser(request, browser, language)
                flag = False


if __name__ == "__main__":
    main()
