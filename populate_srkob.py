# -*- coding: utf-8 -*-
import os

def populate():
    sensacja_gen = add_gen('Sensacja')
    fantasy_gen = add_gen('Fantastyka')
    criminal_gen = add_gen('Kryminał')
    fiary_gen = add_gen('Bajki')
    drama_gen = add_gen('Dramat')


    pratchett_aut = add_aut(fname="Terry", sname="Pratchett")    
    anthony_aut = add_aut(fname="Piers", sname="Anthony")
    clancy_aut = add_aut(fname="Tom", sname="Clancy")
    goscinny_aut = add_aut(fname="Rene", sname="Gościnny")
    christie_aut = add_aut(fname="Agatha", sname="Christie")
    shakespeare_aut = add_aut(fname="William", sname="Shakespeare")
    fredro_aut = add_aut(fname="Aleksander", sname="Fredro")

    
    add_book(title="Zemsta",
             author=fredro_aut,
             about="Cześnik Raptusiewicz i Rejent Milczek mieszkają w jednym zamku. Ich życie upływa na kłótniach i intrygach. Życie Wacława Rejentowicza i Klary Raptusiewiczówny - wprost przeciwnie. Młodzi są zakochani, planują wspólną przyszłość, dlatego robią wszystko, by pogodzić zwaśnionych sąsiadów. Czy pojedynek Cześnika i Rejenta dojdzie do skutku, czy też miłość zatryumfuje nad przemożnym pragnieniem zemsty?",
             gen=drama_gen)

    add_book(title="Polowanie na Czerwony Październik",
             author=clancy_aut,
             about="Zimna wojna. Z radzieckiej bazy wojennej niedaleko portu Murmańsk wypływa okręt podwodny typu Typhoon, tytułowy Czerwony Październik. Dowodzi nim Marko Ramius, wybitny strateg i oficer floty ZSRR. W tym samym czasie Jack Ryan, analityk Centralnej Agencji Wywiadowczej, odkrywa różnice pomiędzy sylwetką Czerwonego Października a innymi radzieckimi podwodnymi okrętami atomowymi – dodatkowe otwory na dziobie i rufie okrętu",
             gen=sensacja_gen)

    add_book(title="Czas Patriotów",
             author=clancy_aut,
             about="Jack Ryan to wykładowca historii w Annapolis, bazie marynarki stanów zjednoczonych. Podczas pobytu z rodziną w Londynie, Jack jest świadkiem zamachu członków irlandzkiej organizacji ULA (Armia Wyzwolenia Ulsteru) na rodzinę królewską. Postanawia on zaryzykować i pomóc atakowanym - pomimo postrzału, ratuje on królewska parę, tym samym rzuca na siebie wyrok ULA. Nawet w USA nie może czuć się już bezpieczny...",
             gen=sensacja_gen)

    add_book(title="Śluby panieńskie",
             author=fredro_aut,
             about="Komedia powstała w 1832 r. Opowiada historię Anieli i Klary, które przysięgły sobie, że nigdy w życiu nie wyjdą za mąż. Fredro pokazuje w swym utworze miłość jako coś cudownego i radosnego - a jednak coś, do czego trzeba wytrwale dążyć, często mimo przeróżnych niepowodzeń.",
             gen=drama_gen)
             
    add_book(title="Kolor Magii",
             author=pratchett_aut,
             about="Głównym bohaterem powieści jest niezbyt zdolny, ale posiadający genialny instynkt przetrwania mag Rincewind. Zostaje on przewodnikiem pierwszego turysty na Dysku: bajecznie bogatego, beztroskiego Dwukwiata. Dzięki ich przygodom, czytelnik poznaje obyczaje, kulturę i geografię świata Dysku i jego największego miasta, Ankh-Morpork, leżącego nad Ankh – jedyną na dysku rzeką, której wodę można kroić nożem.",
             gen=fantasy_gen)         

    add_book(title="Zaklęcie dla Cameleon",
             author=anthony_aut,
             about="Poznajemy głównego bohatera na kilka tygodni przed przełomowym momentem jego życia. Prawem krainy Xanth jest posiadanie talentu magicznego przez każdego człowieka. Bink do tej pory nie odkrył swojego talentu, a za dwa miesiące będzie obchodzić dwudzieste piąte urodziny - chwila, kiedy ostatecznie będzie musiał się z niego wylegitymować.",
             gen=fantasy_gen)
             
    add_book(title="Makbet",
             author=shakespeare_aut,
             about="Macbeth i Banquo, generałowie armii królewskiej, wracając do domów po zwycięskiej bitwie, spotykają na swojej drodze trzy czarownice. Przepowiadają one pierwszemu z nich rychłe wyniesienie na króla, drugiemu pozostawiając jednak przywilej poczęcia królewskiego rodu.",
             gen=drama_gen)
             
    add_book(title="Śmierć w chmurach",
             author=christie_aut,
             about="Zamordowana zostaje słynna paryska lichwiarka, Madame Giselle. Podczas lotu samolotem z Paryża do Croydon, trafia ją zatruta strzałka, wypuszczona z dmuchawki, jakiej używają południowoamerykańskie plemiona. Wiadomo, że winnym tej specyficznej zbrodni musi być ktoś z dwunastu pasażerów, znajdujących się w tej samej części pokładu.",
             gen=criminal_gen)                  

    add_book(title="Wielka czwórka",
             author=christie_aut,
             about="Wielka Czwórka jest to organizacja przestępcza, na której czele stoją cztery wpływowe w świecie osoby. Grupa ta ma odpowiada za wzmożony rozwój przestępstwa na całej kuli ziemskiej i nawet żaden ze światowych rządów nie jest w stanie się im przeciwstawić. Wydaje się, że jeśli ktoś nie położy temu kresu, Wielka Czwórka obejmie władzę nad całym światem, wprowadzając powszechny terror i przestępczość.",
             gen=criminal_gen)
     
    add_book(title="Asteriks Podarunek Cezara.",
             author=goscinny_aut,
             about="Każdy rzymski legionista, któremu udało się przetrwać dwudziestoletnią służbę wojskową, dostawał od Juliusza Cezara niewielką posiadłość ziemską w podbitych krajach. Taki dar otrzymał również Romeomontekus, mimo że jako nałogowy pijak i awanturnik nieustannie sprawiał problemy swoim przełożonym, a w dodatku obrażał samego Cezara. ",
             gen=fiary_gen)
      
    add_book(title="Przepisy Mikołajka",
             author=goscinny_aut,
             about="Mikołajek i jego koledzy są wielkimi łasuchami - i to wcale nie tylko Alcest! A teraz pokazują, że gotowanie może być ogromną frajdą. Szalone szaszłyki, trzypiętrowa kanapka, skaczący popcorn - Przepisy Mikołajka to mnóstwo smacznych i zabawnych dań dla małych i dużych.",
             gen=fiary_gen)
                     
    


                                     
def add_book(title, author, about, gen):
    b = Book.objects.get_or_create(title=title, author=author, about=about, genre=gen)
    return p

def add_aut(fname, sname):
    a = Author.objects.get_or_create(first_name=fname, last_name=sname)  
    return a

def add_gen(name):
    g = Genre.objects.get_or_create(genre_main=name)
    return g

# Start execution here!
if __name__ == '__main__':
    print "Starting Srkob population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biblioteka.settings')
    from srkob.models import Genre, Author, Book
    populate()
