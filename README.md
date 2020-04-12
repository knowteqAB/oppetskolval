# ÖppetSkolval
OpenSkolval är ett initiativ startat av Knowteq AB. Tillsammans med kommuner vill vi skapa Sveriges första skolvals-system som öppen källkod. Detta innebär att systemet är fritt att
använda, helt utan licens-avgifter för kommuner. Målet är ett system som garanterar
lagliga och rättvisa skolplaceringar med full transparens mot kommuner och vårdnadshavare.

OpenSkolval är en modulbaserad system-lösning för skolval som kan användas som helhetslösning, eller enbart för att skapa placeringar.

## Varför ÖppetSkolval
Det finns idag ett antal aktörer på skolvals-marknaden och kommuner som inför aktivt
skolval väljer vanligtvis att anlita någon av dessa för att automatisera urvalet till
grundskolan. Att byta leverantör kan vara kostsamt och kommunen blir därför i många fall
låsta till en system-lösning under lång tid. 

Vi som driver ÖppetSkolval tycker att det är en dålig lösning som leder till att
riktlinjer för skolval till stor del definieras av de lösningar som erbjuds av befintliga
systemleverantör. Dessutom saknas incitament hos leverantörerna att själva driva
vidareutveckling av urvalsmetoder då kommunerna ofta är inlåsta. 

ÖppetSkolval grundas i ett engagerade att tillsammans med kommuner ta fram metoder
som skapar lagliga, rättvisa och rimliga placeringar. Vi anser att dagen lösning med
stängda system av flera skäl inte är en lämplig lösning för kommuner som 
erbjuder aktivt skolval till grundskolan. En del kommuner har idag egen systemutveckling
vilket är kostsamt och kräver stora arbetsinsatser från kommunen i form av kravställning
och uppföljning. Vi tycker att kommuner bör sammarbeta för att ta fram systemlösningar.
 
## Varför öppen källkod
Skolval och urvalsprinciper ser väldigt lika ut i Sveriges olika kommuner och de flesta 
kommuner har idag skolval med urvalsgrunden "relativ närhet". Att kommuner tillsammans
utvecklar en systemlösning för skolval som dessutom är öppen källkod är en kostnadseffektiv och 
långsiktig lösning som skapar transparens mot medborgare. Kommuner kan fritt vidareutveckla 
ÖppetSkolval för att skapa urvalskriterier i enlighet med de riktlinjer som kommunen antagit
i de fall detta inte redan stöds.  

För vårdnashavare innebär öppen källkod att urvalet till skola blir helt transparent.
Alla med grundläggande kunskap om programmering har möjlighet att granska den kod som
används vid skolplacering vilket inte är möjligt med stängda skolplacerings-system.

## Placeringsalgoritmer
Att placera enligt relativ närhet innebär att alla elever ansöker till sitt skolval
med en poäng baserat på differensen mellan avståndet till den sökta kolan och en 
alternativ placering (X - A där X är den sökta skolan och A är den alternativ placeringen).

Det som i huvudsak skiljer skolvalsalgoritmer är hur den alternativa placeringen
definieras.

### Knowteq skolval, Relativ närhet - på rätt sätt
Knowteqs skolval stödjer urvalsprincipen "relativ närhet" med närhetspoäng baserat på 
garantiskolor. Garantiskolor beräknas för alla elever samtidigt med välbeprövade 
optimeringstekniker. Varje elevs garantiskola är den skola som garanterar att den
totala gångsträckan för samtliga elever minimeras.

Vid beräkning av närhetspoäng används altid garantiskolan som alternativ placering. I det
fall en elev ansöker till sin garantiskola antas en oändligt hög poäng vilket garanterar
placering.

