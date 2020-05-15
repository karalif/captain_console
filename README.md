
## Captain Console
Captain Console online website

### Tilgangur
Læra að setja upp vefsíðu frá grunni með hjálp Django, ElephantSQL og Python þar sem aðal áskorunin er að setja saman ýmsar mismunandi skrár og láta þær tala saman og skila heilstæðu kerfi. 

### Lýsing
Þessi vefsíða er fyrsta tilvist verslunarinnar Captain Console á internetinu. Markmið vefsíðunarinnar er að bjóða upp á víðtækt og spennandi úrval gamaldags leikjatalva og leikja. Þessi vefsíða á að hjálpa fyrirtækinu að stækka og dafna í heimi vefverslanna þar sem hún gerir viðskiptavinum kleift að nálgast vörur á einfaldan og þægilegan máta og veitir þeim helstu upplýsingar um hverja vöru fyrir sig.

### Að byrja

Eftirfarandi leiðbeiningar munu aðstoða við uppsetningu kerfisins.

Fyrsta sem þarf að gera er að búa til virtual environment og setja inn í möppu verkefnisins. Það gerir maður í gegnum Django, pure python file. 

Vinsamlegast keyrið eftirfarandi skipun í terminal til þess að tengja venv.  

    $source venv/bin/activate

Sjá kaflann um Niðurhöl áður en haldið er áfram í þessum kafla.

Þegar venv mappan er komin inn í möppu verkefnisins og tengd þá á að fylgja eftirfarandi skrefnum til þess að keyra upp vefsíðuna á vafranum þínum. 

    $python manage.py runserver
    
VANTAR SMÁ TEXTA HÉR UM ÞESSA SKIPUN

    $python manage.py runserver --insecure

Ef farið er inná 127.0.0.1:8000/admin fæst eftirfarandi villumelding: Python quit unexpectedly. Í þessu tilfelli þarf að endurkeyra síðuna í gegnum terminal og best væri að skrá sig inn undir log in hnappi efst á hægri horni síðunnar og nota þar admin notendanafn og lykilorð.

Einnig er vert að taka fram að villumeldingar virka einungis ef að DEBUG=False og allowed_hosts=['*'].

### Niðurhöl
Hér má sjá allt sem sem þarf að hlaða niður áður en verkefnið er keyrt upp á vafranum.

    $pip install psycopg2-binary 

### Bónus stig
Í þessum kafla er listað upp allt það sem við gerðum umfram verkefnalýsingu og mun teljast til aukastiga. 

Hægt er að ýta á "profile" og þar sérst yfirlit. Einnig er hægt að fara af profile á update profile síðu.  

Admin getur búið til nýja vöru fyrir síðuna, uppfært vörur og eytt þeim af síðunni.

### Built With
* HTML5  - Nýjasta útgáfa af HyperText Markup Language.
* CSS3 - Style Sheet Language sem stýlar HTML5 skjöl.

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

### Eigendur
Arndís Einarsdóttir <br>
Helga Lárusdóttir<br>
Katla Rún Arnórsdóttir <br>
Kara Líf Ingibergsdóttir

