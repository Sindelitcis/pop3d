# Política de Privacidade do Pop3D em todos os idiomas do site (o significado precisa ser o mesmo em todos).
# Mudou algo no que o app coleta? Atualize todas e a DATA.

DATA = {"pt": "2 de outubro de 2026", "en": "October 2, 2026", "es": "2 de octubre de 2026", "fr": "2 octobre 2026",
        "de": "2. Oktober 2026", "it": "2 ottobre 2026", "uk": "2 жовтня 2026 р.",
        "sv": "2 oktober 2026", "ja": "2026年10月2日", "zh": "2026年10月2日",
        "nl": "2 oktober 2026", "hu": "2026. október 2.", "ru": "2 октября 2026 г.", "ko": "2026년 10월 2일",
        "zh-hans": "2026年10月2日"}
ISSUES = '<a href="https://github.com/Sindelitcis/pop3d/issues">github.com/Sindelitcis/pop3d/issues</a>'

PT = {"titulo": "Política de Privacidade", "atualizada": "Atualizada em", "inicio": "Página inicial", "corpo": f"""
<div class="resumo"><p><b>Resumo:</b> seus filmes e vídeos nunca saem do seu computador. O Pop3D só envia estatísticas anônimas de uso (como o modelo da placa de vídeo e o desempenho) para a gente melhorar o app, e você pode desligar isso a qualquer momento nos Ajustes.</p></div>
<h2>Quem somos</h2>
<p>O Pop3D é um aplicativo gratuito que transforma vídeos 2D em 3D para óculos de realidade virtual. Ele é formado pelo aplicativo do computador (Windows) e pelo aplicativo do óculos (Meta Quest). Esta política vale para os dois.</p>
<h2>O que nunca coletamos</h2>
<ul>
<li>Nomes, conteúdos ou imagens dos seus filmes e vídeos, nem o que aparece na tela do seu computador.</li>
<li>Nomes de pastas e arquivos do seu computador.</li>
<li>Seu nome, contas, contatos ou qualquer dado que identifique você (o e-mail só se você mesmo escrever numa sugestão; veja abaixo).</li>
<li>Seu endereço IP: ele não é guardado nem usado para descobrir onde você está.</li>
<li>Imagens das câmeras, do ambiente ou dos movimentos do óculos.</li>
</ul>
<p>Todo o processamento acontece no seu próprio computador. O vídeo vai do computador para o óculos pela sua rede local (Wi-Fi ou cabo), sem passar pela internet.</p>
<h2>O que coletamos (estatísticas anônimas de uso)</h2>
<p>Para descobrir problemas e deixar o app mais rápido em mais computadores, o aplicativo do computador envia informações técnicas como:</p>
<ul>
<li>Um código aleatório criado na instalação, que não tem relação com você (serve só para contar instalações sem duplicar).</li>
<li>Versão do Pop3D e do Windows, idioma do sistema e do app.</li>
<li>Modelo da placa de vídeo, memória de vídeo, versão do driver, processador e memória RAM.</li>
<li>Resultados de desempenho: quadros por segundo, uso da placa de vídeo e a qualidade escolhida.</li>
<li>Como o app é usado: tipo de óculos e de conexão (Wi-Fi, cabo, PC VR), modo de vídeo (2D, 3D, tela do PC), tempo de uso.</li>
<li>Etapas da instalação e mensagens de erro (sem nomes de arquivos ou pastas). Quando acontece um erro ou o vídeo trava, vão junto as últimas linhas do registro técnico do app, limpas antes de sair do computador: sem nomes de filmes, arquivos, pastas, e-mails ou endereços IP.</li>
</ul>
<p>Esses dados são guardados pelo <b>PostHog</b>, um serviço de estatísticas, em servidores na <b>União Europeia</b>, e só são vistos pela equipe do Pop3D. Não vendemos nem compartilhamos esses dados com mais ninguém, e não os usamos para propaganda.</p>
<h2>Sugestões que você nos manda</h2>
<p>Em <b>Ideias e sugestões</b>, dentro do app, você pode nos mandar uma mensagem. Junto com o texto que você escrever vão a versão do app e o modelo da placa de vídeo. O e-mail é <b>opcional</b>: só vai se você preencher, e só é usado para responder a sua mensagem. As sugestões ficam guardadas no mesmo serviço das estatísticas (PostHog, União Europeia). Elas são enviadas mesmo com as estatísticas desligadas, porque é você que decide mandar.</p>
<h2>Como desligar</h2>
<p>No aplicativo do computador, abra <b>Ajustes</b> e desligue <b>Enviar dados de uso anônimos</b>. A partir daí, nada mais é enviado (só as sugestões que você mesmo mandar).</p>
<h2>Atualizações</h2>
<p>Ao abrir, o Pop3D consulta o <b>GitHub</b> (onde as versões são publicadas) para saber se saiu uma versão nova. Como qualquer site, o GitHub recebe o endereço de internet do seu computador nesse momento; a política de privacidade do GitHub vale para essa consulta. Nenhuma informação sua é enviada junto.</p>
<h2>Aplicativo do óculos (Meta Quest)</h2>
<p>O aplicativo Pop3D do óculos não coleta nem envia dados para a internet. Ele só conversa com o seu computador, na sua rede local, para receber o vídeo e mandar os comandos dos controles.</p>
<h2>Crianças</h2>
<p>O Pop3D não coleta dados pessoais de ninguém, inclusive de crianças. Siga as recomendações de idade da fabricante do seu óculos.</p>
<h2>Seus direitos (LGPD e GDPR)</h2>
<p>Como as estatísticas são anônimas, não conseguimos ligá-las a você. Mesmo assim, se quiser que apaguemos as estatísticas do seu computador ou uma sugestão que você mandou, fale com a gente pelo link abaixo, informando o código de instalação que aparece nos Ajustes.</p>
<h2>Mudanças nesta política</h2>
<p>Se esta política mudar, a nova versão aparece nesta página com a data atualizada.</p>
<h2>Contato</h2>
<p>Dúvidas ou pedidos: {ISSUES}.</p>
"""}

EN = {"titulo": "Privacy Policy", "atualizada": "Updated on", "inicio": "Home", "corpo": f"""
<div class="resumo"><p><b>In short:</b> your movies and videos never leave your computer. Pop3D only sends anonymous usage statistics (such as your graphics card model and performance) so we can improve the app, and you can turn this off at any time in Settings.</p></div>
<h2>Who we are</h2>
<p>Pop3D is a free app that turns 2D videos into 3D for virtual reality headsets. It is made of the computer app (Windows) and the headset app (Meta Quest). This policy covers both.</p>
<h2>What we never collect</h2>
<ul>
<li>Names, content or images of your movies and videos, or anything shown on your computer screen.</li>
<li>Names of folders and files on your computer.</li>
<li>Your name, accounts, contacts or any data that identifies you (an email address only if you type it into a suggestion yourself; see below).</li>
<li>Your IP address: it is not stored or used to find out where you are.</li>
<li>Camera images, your surroundings or headset movements.</li>
</ul>
<p>All processing happens on your own computer. Video travels from your computer to your headset over your local network (Wi-Fi or cable), never through the internet.</p>
<h2>What we collect (anonymous usage statistics)</h2>
<p>To find problems and make the app faster on more computers, the computer app sends technical information such as:</p>
<ul>
<li>A random code created at installation, unrelated to you (used only to count installations without duplicates).</li>
<li>Pop3D and Windows versions, system and app language.</li>
<li>Graphics card model, video memory, driver version, processor and RAM.</li>
<li>Performance results: frames per second, graphics card usage and the chosen quality.</li>
<li>How the app is used: headset and connection type (Wi-Fi, cable, PC VR), video mode (2D, 3D, PC screen), usage time.</li>
<li>Installation steps and error messages (without file or folder names). When an error happens or the video freezes, the last lines of the app's technical log go along, cleaned before they leave the computer: no movie, file or folder names, e-mails or IP addresses.</li>
</ul>
<p>This data is stored by <b>PostHog</b>, an analytics service, on servers in the <b>European Union</b>, and is only seen by the Pop3D team. We do not sell or share this data with anyone else, and we do not use it for advertising.</p>
<h2>Suggestions you send us</h2>
<p>Under <b>Ideas &amp; feedback</b>, inside the app, you can send us a message. Along with the text you write, the app version and your graphics card model are sent. Your email is <b>optional</b>: it is only sent if you fill it in, and it is only used to reply to your message. Suggestions are stored in the same service as the statistics (PostHog, European Union). They are sent even with statistics turned off, because you choose to send them.</p>
<h2>How to turn it off</h2>
<p>In the computer app, open <b>Settings</b> and turn off <b>Send anonymous usage data</b>. From then on, nothing else is sent (except suggestions you choose to send).</p>
<h2>Updates</h2>
<p>When it opens, Pop3D checks <b>GitHub</b> (where versions are published) to see if a new version is out. Like any website, GitHub receives your computer's internet address at that moment; GitHub's privacy policy applies to that check. None of your information is sent with it.</p>
<h2>Headset app (Meta Quest)</h2>
<p>The Pop3D headset app does not collect or send any data to the internet. It only talks to your computer, on your local network, to receive video and send controller input.</p>
<h2>Children</h2>
<p>Pop3D does not collect personal data from anyone, including children. Follow your headset maker's age recommendations.</p>
<h2>Your rights (LGPD and GDPR)</h2>
<p>Since the statistics are anonymous, we cannot link them to you. Even so, if you want us to delete your computer's statistics or a suggestion you sent, contact us at the link below with the installation code shown in Settings.</p>
<h2>Changes to this policy</h2>
<p>If this policy changes, the new version will appear on this page with an updated date.</p>
<h2>Contact</h2>
<p>Questions or requests: {ISSUES}.</p>
"""}

ES = {"titulo": "Política de Privacidad", "atualizada": "Actualizada el", "inicio": "Inicio", "corpo": f"""
<div class="resumo"><p><b>En resumen:</b> tus películas y videos nunca salen de tu computadora. Pop3D solo envía estadísticas anónimas de uso (como el modelo de la tarjeta gráfica y el rendimiento) para que podamos mejorar la app, y puedes desactivarlo en cualquier momento en Ajustes.</p></div>
<h2>Quiénes somos</h2>
<p>Pop3D es una app gratuita que convierte videos 2D en 3D para visores de realidad virtual. Está formada por la app de la computadora (Windows) y la app del visor (Meta Quest). Esta política vale para las dos.</p>
<h2>Lo que nunca recopilamos</h2>
<ul>
<li>Nombres, contenidos o imágenes de tus películas y videos, ni lo que aparece en la pantalla de tu computadora.</li>
<li>Nombres de carpetas y archivos de tu computadora.</li>
<li>Tu nombre, cuentas, contactos ni ningún dato que te identifique (el correo solo si tú mismo lo escribes en una sugerencia; ver abajo).</li>
<li>Tu dirección IP: no se guarda ni se usa para saber dónde estás.</li>
<li>Imágenes de las cámaras, del entorno o de los movimientos del visor.</li>
</ul>
<p>Todo el procesamiento ocurre en tu propia computadora. El video va de la computadora al visor por tu red local (Wi-Fi o cable), sin pasar por internet.</p>
<h2>Lo que recopilamos (estadísticas anónimas de uso)</h2>
<p>Para encontrar problemas y hacer la app más rápida en más computadoras, la app de la computadora envía información técnica como:</p>
<ul>
<li>Un código aleatorio creado en la instalación, sin relación contigo (solo sirve para contar instalaciones sin duplicar).</li>
<li>Versión de Pop3D y de Windows, idioma del sistema y de la app.</li>
<li>Modelo de la tarjeta gráfica, memoria de video, versión del controlador, procesador y memoria RAM.</li>
<li>Resultados de rendimiento: cuadros por segundo, uso de la tarjeta gráfica y la calidad elegida.</li>
<li>Cómo se usa la app: tipo de visor y de conexión (Wi-Fi, cable, PC VR), modo de video (2D, 3D, pantalla de la PC), tiempo de uso.</li>
<li>Pasos de la instalación y mensajes de error (sin nombres de archivos ni carpetas). Cuando ocurre un error o el video se traba, van también las últimas líneas del registro técnico de la app, limpias antes de salir de la computadora: sin nombres de películas, archivos, carpetas, correos ni direcciones IP.</li>
</ul>
<p>Estos datos se guardan en <b>PostHog</b>, un servicio de estadísticas, en servidores de la <b>Unión Europea</b>, y solo los ve el equipo de Pop3D. No vendemos ni compartimos estos datos con nadie más, y no los usamos para publicidad.</p>
<h2>Sugerencias que nos envías</h2>
<p>En <b>Ideas y sugerencias</b>, dentro de la app, puedes enviarnos un mensaje. Junto con el texto que escribas se envían la versión de la app y el modelo de la tarjeta gráfica. El correo es <b>opcional</b>: solo se envía si lo completas, y solo se usa para responder tu mensaje. Las sugerencias se guardan en el mismo servicio que las estadísticas (PostHog, Unión Europea). Se envían aunque las estadísticas estén desactivadas, porque tú decides enviarlas.</p>
<h2>Cómo desactivarlo</h2>
<p>En la app de la computadora, abre <b>Ajustes</b> y desactiva <b>Enviar datos de uso anónimos</b>. A partir de ahí, no se envía nada más (solo las sugerencias que tú decidas enviar).</p>
<h2>Actualizaciones</h2>
<p>Al abrirse, Pop3D consulta <b>GitHub</b> (donde se publican las versiones) para saber si salió una versión nueva. Como cualquier sitio web, GitHub recibe la dirección de internet de tu computadora en ese momento; la política de privacidad de GitHub vale para esa consulta. No se envía ninguna información tuya.</p>
<h2>App del visor (Meta Quest)</h2>
<p>La app Pop3D del visor no recopila ni envía datos a internet. Solo se comunica con tu computadora, en tu red local, para recibir el video y enviar los comandos de los controles.</p>
<h2>Niños</h2>
<p>Pop3D no recopila datos personales de nadie, incluidos los niños. Sigue las recomendaciones de edad del fabricante de tu visor.</p>
<h2>Tus derechos (LGPD y GDPR)</h2>
<p>Como las estadísticas son anónimas, no podemos vincularlas contigo. Aun así, si quieres que borremos las estadísticas de tu computadora o una sugerencia que enviaste, escríbenos en el enlace de abajo indicando el código de instalación que aparece en Ajustes.</p>
<h2>Cambios en esta política</h2>
<p>Si esta política cambia, la nueva versión aparecerá en esta página con la fecha actualizada.</p>
<h2>Contacto</h2>
<p>Dudas o pedidos: {ISSUES}.</p>
"""}

FR = {"titulo": "Politique de confidentialité", "atualizada": "Mise à jour le", "inicio": "Accueil", "corpo": f"""
<div class="resumo"><p><b>En bref :</b> vos films et vidéos ne quittent jamais votre ordinateur. Pop3D envoie uniquement des statistiques d'utilisation anonymes (comme le modèle de la carte graphique et les performances) pour que nous puissions améliorer l'app, et vous pouvez les désactiver à tout moment dans les Réglages.</p></div>
<h2>Qui sommes-nous</h2>
<p>Pop3D est une application gratuite qui transforme les vidéos 2D en 3D pour les casques de réalité virtuelle. Elle se compose de l'application pour ordinateur (Windows) et de l'application pour casque (Meta Quest). Cette politique s'applique aux deux.</p>
<h2>Ce que nous ne collectons jamais</h2>
<ul>
<li>Les noms, contenus ou images de vos films et vidéos, ni ce qui s'affiche sur l'écran de votre ordinateur.</li>
<li>Les noms des dossiers et fichiers de votre ordinateur.</li>
<li>Votre nom, vos comptes, vos contacts ou toute donnée qui vous identifie (l'e-mail uniquement si vous l'écrivez vous-même dans une suggestion ; voir plus bas).</li>
<li>Votre adresse IP : elle n'est ni conservée ni utilisée pour savoir où vous vous trouvez.</li>
<li>Les images des caméras, de votre environnement ou des mouvements du casque.</li>
</ul>
<p>Tout le traitement se fait sur votre propre ordinateur. La vidéo passe de l'ordinateur au casque par votre réseau local (Wi-Fi ou câble), sans passer par internet.</p>
<h2>Ce que nous collectons (statistiques d'utilisation anonymes)</h2>
<p>Pour détecter les problèmes et rendre l'app plus rapide sur plus d'ordinateurs, l'application pour ordinateur envoie des informations techniques comme :</p>
<ul>
<li>Un code aléatoire créé à l'installation, sans lien avec vous (il sert seulement à compter les installations sans doublon).</li>
<li>Les versions de Pop3D et de Windows, la langue du système et de l'app.</li>
<li>Le modèle de la carte graphique, la mémoire vidéo, la version du pilote, le processeur et la mémoire vive.</li>
<li>Les résultats de performances : images par seconde, utilisation de la carte graphique et qualité choisie.</li>
<li>La façon dont l'app est utilisée : type de casque et de connexion (Wi-Fi, câble, PC VR), mode vidéo (2D, 3D, écran du PC), durée d'utilisation.</li>
<li>Les étapes de l'installation et les messages d'erreur (sans noms de fichiers ni de dossiers). Lorsqu'une erreur se produit ou que la vidéo se bloque, les dernières lignes du journal technique de l'app sont jointes, nettoyées avant de quitter l'ordinateur : sans noms de films, de fichiers, de dossiers, d'e-mails ni d'adresses IP.</li>
</ul>
<p>Ces données sont conservées par <b>PostHog</b>, un service de statistiques, sur des serveurs situés dans l'<b>Union européenne</b>, et ne sont consultées que par l'équipe de Pop3D. Nous ne vendons ni ne partageons ces données avec personne, et nous ne les utilisons pas pour de la publicité.</p>
<h2>Les suggestions que vous nous envoyez</h2>
<p>Dans <b>Idées et suggestions</b>, dans l'app, vous pouvez nous envoyer un message. Avec le texte que vous écrivez sont envoyés la version de l'app et le modèle de la carte graphique. L'e-mail est <b>facultatif</b> : il n'est envoyé que si vous le remplissez, et sert uniquement à vous répondre. Les suggestions sont conservées dans le même service que les statistiques (PostHog, Union européenne). Elles sont envoyées même si les statistiques sont désactivées, car c'est vous qui décidez de les envoyer.</p>
<h2>Comment désactiver</h2>
<p>Dans l'application pour ordinateur, ouvrez les <b>Réglages</b> et désactivez <b>Envoyer des données d'utilisation anonymes</b>. À partir de là, plus rien n'est envoyé (sauf les suggestions que vous choisissez d'envoyer).</p>
<h2>Mises à jour</h2>
<p>À l'ouverture, Pop3D consulte <b>GitHub</b> (où les versions sont publiées) pour savoir si une nouvelle version est sortie. Comme n'importe quel site, GitHub reçoit alors l'adresse internet de votre ordinateur ; la politique de confidentialité de GitHub s'applique à cette consultation. Aucune information vous concernant n'est envoyée avec.</p>
<h2>Application du casque (Meta Quest)</h2>
<p>L'application Pop3D du casque ne collecte ni n'envoie aucune donnée sur internet. Elle communique uniquement avec votre ordinateur, sur votre réseau local, pour recevoir la vidéo et envoyer les commandes des manettes.</p>
<h2>Enfants</h2>
<p>Pop3D ne collecte de données personnelles sur personne, y compris les enfants. Suivez les recommandations d'âge du fabricant de votre casque.</p>
<h2>Vos droits (RGPD et LGPD)</h2>
<p>Comme les statistiques sont anonymes, nous ne pouvons pas les relier à vous. Malgré tout, si vous souhaitez que nous supprimions les statistiques de votre ordinateur ou une suggestion que vous avez envoyée, contactez-nous via le lien ci-dessous en indiquant le code d'installation affiché dans les Réglages.</p>
<h2>Modifications de cette politique</h2>
<p>Si cette politique change, la nouvelle version apparaîtra sur cette page avec la date mise à jour.</p>
<h2>Contact</h2>
<p>Questions ou demandes : {ISSUES}.</p>
"""}

DE = {"titulo": "Datenschutzerklärung", "atualizada": "Aktualisiert am", "inicio": "Startseite", "corpo": f"""
<div class="resumo"><p><b>Kurz gesagt:</b> Deine Filme und Videos verlassen nie deinen Computer. Pop3D sendet nur anonyme Nutzungsstatistiken (zum Beispiel das Grafikkartenmodell und die Leistung), damit wir die App verbessern können, und du kannst das jederzeit in den Einstellungen ausschalten.</p></div>
<h2>Wer wir sind</h2>
<p>Pop3D ist eine kostenlose App, die 2D-Videos für Virtual-Reality-Headsets in 3D umwandelt. Sie besteht aus der Computer-App (Windows) und der Headset-App (Meta Quest). Diese Erklärung gilt für beide.</p>
<h2>Was wir nie erfassen</h2>
<ul>
<li>Namen, Inhalte oder Bilder deiner Filme und Videos oder das, was auf deinem Computerbildschirm angezeigt wird.</li>
<li>Namen von Ordnern und Dateien auf deinem Computer.</li>
<li>Deinen Namen, Konten, Kontakte oder sonstige Daten, die dich identifizieren (eine E-Mail-Adresse nur, wenn du sie selbst in einen Vorschlag schreibst; siehe unten).</li>
<li>Deine IP-Adresse: Sie wird weder gespeichert noch genutzt, um herauszufinden, wo du bist.</li>
<li>Kamerabilder, deine Umgebung oder Bewegungen des Headsets.</li>
</ul>
<p>Die gesamte Verarbeitung findet auf deinem eigenen Computer statt. Das Video gelangt über dein lokales Netzwerk (WLAN oder Kabel) vom Computer ins Headset, nie über das Internet.</p>
<h2>Was wir erfassen (anonyme Nutzungsstatistiken)</h2>
<p>Um Probleme zu finden und die App auf mehr Computern schneller zu machen, sendet die Computer-App technische Informationen wie:</p>
<ul>
<li>Einen bei der Installation erzeugten Zufallscode, der nichts mit dir zu tun hat (er dient nur dazu, Installationen ohne Doppelzählung zu zählen).</li>
<li>Version von Pop3D und Windows, Sprache des Systems und der App.</li>
<li>Grafikkartenmodell, Videospeicher, Treiberversion, Prozessor und Arbeitsspeicher.</li>
<li>Leistungswerte: Bilder pro Sekunde, Auslastung der Grafikkarte und gewählte Qualität.</li>
<li>Wie die App genutzt wird: Art des Headsets und der Verbindung (WLAN, Kabel, PC-VR), Videomodus (2D, 3D, PC-Bildschirm), Nutzungsdauer.</li>
<li>Installationsschritte und Fehlermeldungen (ohne Datei- oder Ordnernamen). Wenn ein Fehler auftritt oder das Video hängen bleibt, werden die letzten Zeilen des technischen Protokolls der App mitgeschickt, bereinigt, bevor sie den Computer verlassen: ohne Film-, Datei- oder Ordnernamen, E-Mail-Adressen oder IP-Adressen.</li>
</ul>
<p>Diese Daten werden von <b>PostHog</b>, einem Statistikdienst, auf Servern in der <b>Europäischen Union</b> gespeichert und nur vom Pop3D-Team eingesehen. Wir verkaufen diese Daten nicht, geben sie an niemanden weiter und nutzen sie nicht für Werbung.</p>
<h2>Vorschläge, die du uns schickst</h2>
<p>Unter <b>Ideen &amp; Feedback</b> in der App kannst du uns eine Nachricht schicken. Zusammen mit deinem Text werden die App-Version und das Grafikkartenmodell gesendet. Die E-Mail-Adresse ist <b>freiwillig</b>: Sie wird nur gesendet, wenn du sie einträgst, und nur genutzt, um dir zu antworten. Vorschläge werden im selben Dienst wie die Statistiken gespeichert (PostHog, Europäische Union). Sie werden auch bei ausgeschalteten Statistiken gesendet, weil du selbst entscheidest, sie zu schicken.</p>
<h2>So schaltest du es aus</h2>
<p>Öffne in der Computer-App die <b>Einstellungen</b> und schalte <b>Anonyme Nutzungsdaten senden</b> aus. Ab dann wird nichts mehr gesendet (außer Vorschlägen, die du selbst schickst).</p>
<h2>Updates</h2>
<p>Beim Öffnen fragt Pop3D bei <b>GitHub</b> (wo die Versionen veröffentlicht werden) nach, ob es eine neue Version gibt. Wie jede Website erhält GitHub dabei die Internetadresse deines Computers; für diese Abfrage gilt die Datenschutzerklärung von GitHub. Es werden keine Informationen über dich mitgesendet.</p>
<h2>Headset-App (Meta Quest)</h2>
<p>Die Pop3D-App im Headset erfasst keine Daten und sendet nichts ins Internet. Sie kommuniziert nur über dein lokales Netzwerk mit deinem Computer, um das Video zu empfangen und die Controller-Eingaben zu senden.</p>
<h2>Kinder</h2>
<p>Pop3D erfasst von niemandem personenbezogene Daten, auch nicht von Kindern. Beachte die Altersempfehlungen des Herstellers deines Headsets.</p>
<h2>Deine Rechte (DSGVO und LGPD)</h2>
<p>Da die Statistiken anonym sind, können wir sie nicht mit dir in Verbindung bringen. Wenn du trotzdem möchtest, dass wir die Statistiken deines Computers oder einen von dir gesendeten Vorschlag löschen, kontaktiere uns über den Link unten und nenne den Installationscode, der in den Einstellungen angezeigt wird.</p>
<h2>Änderungen dieser Erklärung</h2>
<p>Wenn sich diese Erklärung ändert, erscheint die neue Version auf dieser Seite mit aktualisiertem Datum.</p>
<h2>Kontakt</h2>
<p>Fragen oder Anliegen: {ISSUES}.</p>
"""}

IT = {"titulo": "Informativa sulla privacy", "atualizada": "Aggiornata il", "inicio": "Home", "corpo": f"""
<div class="resumo"><p><b>In breve:</b> i tuoi film e video non lasciano mai il tuo computer. Pop3D invia solo statistiche di utilizzo anonime (come il modello della scheda video e le prestazioni) per permetterci di migliorare l'app, e puoi disattivarle in qualsiasi momento nelle Impostazioni.</p></div>
<h2>Chi siamo</h2>
<p>Pop3D è un'app gratuita che trasforma i video 2D in 3D per i visori di realtà virtuale. È composta dall'app per computer (Windows) e dall'app per visore (Meta Quest). Questa informativa vale per entrambe.</p>
<h2>Cosa non raccogliamo mai</h2>
<ul>
<li>Nomi, contenuti o immagini dei tuoi film e video, né ciò che appare sullo schermo del tuo computer.</li>
<li>Nomi di cartelle e file del tuo computer.</li>
<li>Il tuo nome, account, contatti o qualsiasi dato che ti identifichi (l'e-mail solo se la scrivi tu in un suggerimento; vedi sotto).</li>
<li>Il tuo indirizzo IP: non viene conservato né usato per sapere dove ti trovi.</li>
<li>Immagini delle telecamere, dell'ambiente o dei movimenti del visore.</li>
</ul>
<p>Tutta l'elaborazione avviene sul tuo computer. Il video va dal computer al visore tramite la tua rete locale (Wi-Fi o cavo), senza passare da internet.</p>
<h2>Cosa raccogliamo (statistiche di utilizzo anonime)</h2>
<p>Per individuare problemi e rendere l'app più veloce su più computer, l'app per computer invia informazioni tecniche come:</p>
<ul>
<li>Un codice casuale creato durante l'installazione, senza legami con te (serve solo a contare le installazioni senza duplicati).</li>
<li>Versione di Pop3D e di Windows, lingua del sistema e dell'app.</li>
<li>Modello della scheda video, memoria video, versione del driver, processore e memoria RAM.</li>
<li>Risultati delle prestazioni: fotogrammi al secondo, utilizzo della scheda video e qualità scelta.</li>
<li>Come viene usata l'app: tipo di visore e di connessione (Wi-Fi, cavo, PC VR), modalità video (2D, 3D, schermo del PC), tempo di utilizzo.</li>
<li>Fasi dell'installazione e messaggi di errore (senza nomi di file o cartelle). Quando si verifica un errore o il video si blocca, vengono inviate anche le ultime righe del registro tecnico dell'app, ripulite prima di lasciare il computer: senza nomi di film, file, cartelle, e-mail o indirizzi IP.</li>
</ul>
<p>Questi dati sono conservati da <b>PostHog</b>, un servizio di statistiche, su server nell'<b>Unione europea</b>, e sono visti solo dal team di Pop3D. Non vendiamo né condividiamo questi dati con nessun altro e non li usiamo per la pubblicità.</p>
<h2>I suggerimenti che ci invii</h2>
<p>In <b>Idee e suggerimenti</b>, nell'app, puoi inviarci un messaggio. Insieme al testo che scrivi vengono inviati la versione dell'app e il modello della scheda video. L'e-mail è <b>facoltativa</b>: viene inviata solo se la inserisci, e viene usata solo per risponderti. I suggerimenti sono conservati nello stesso servizio delle statistiche (PostHog, Unione europea). Vengono inviati anche con le statistiche disattivate, perché sei tu a decidere di inviarli.</p>
<h2>Come disattivarle</h2>
<p>Nell'app per computer, apri le <b>Impostazioni</b> e disattiva <b>Invia dati di utilizzo anonimi</b>. Da quel momento non viene inviato più nulla (tranne i suggerimenti che decidi di inviare tu).</p>
<h2>Aggiornamenti</h2>
<p>All'apertura, Pop3D consulta <b>GitHub</b> (dove vengono pubblicate le versioni) per sapere se è uscita una nuova versione. Come qualsiasi sito, in quel momento GitHub riceve l'indirizzo internet del tuo computer; a questa richiesta si applica l'informativa sulla privacy di GitHub. Non viene inviata nessuna informazione su di te.</p>
<h2>App del visore (Meta Quest)</h2>
<p>L'app Pop3D del visore non raccoglie né invia dati su internet. Comunica solo con il tuo computer, sulla tua rete locale, per ricevere il video e inviare i comandi dei controller.</p>
<h2>Minori</h2>
<p>Pop3D non raccoglie dati personali di nessuno, compresi i minori. Segui le indicazioni sull'età del produttore del tuo visore.</p>
<h2>I tuoi diritti (GDPR e LGPD)</h2>
<p>Poiché le statistiche sono anonime, non possiamo collegarle a te. Se comunque vuoi che cancelliamo le statistiche del tuo computer o un suggerimento che hai inviato, contattaci tramite il link qui sotto indicando il codice di installazione mostrato nelle Impostazioni.</p>
<h2>Modifiche a questa informativa</h2>
<p>Se questa informativa cambia, la nuova versione apparirà in questa pagina con la data aggiornata.</p>
<h2>Contatti</h2>
<p>Domande o richieste: {ISSUES}.</p>
"""}

UK = {"titulo": "Політика конфіденційності", "atualizada": "Оновлено", "inicio": "Головна", "corpo": f"""
<div class="resumo"><p><b>Коротко:</b> ваші фільми й відео ніколи не залишають ваш комп'ютер. Pop3D надсилає лише анонімну статистику використання (наприклад, модель відеокарти та продуктивність), щоб ми могли покращувати застосунок, і її можна будь-коли вимкнути в Налаштуваннях.</p></div>
<h2>Хто ми</h2>
<p>Pop3D — безкоштовний застосунок, який перетворює 2D-відео на 3D для шоломів віртуальної реальності. Він складається із застосунку для комп'ютера (Windows) і застосунку для шолома (Meta Quest). Ця політика стосується обох.</p>
<h2>Що ми ніколи не збираємо</h2>
<ul>
<li>Назви, вміст чи зображення ваших фільмів і відео, а також те, що показується на екрані вашого комп'ютера.</li>
<li>Назви папок і файлів на вашому комп'ютері.</li>
<li>Ваше ім'я, облікові записи, контакти чи будь-які дані, що вас ідентифікують (e-mail — лише якщо ви самі вкажете його в пропозиції; див. нижче).</li>
<li>Вашу IP-адресу: вона не зберігається і не використовується, щоб визначити, де ви перебуваєте.</li>
<li>Зображення з камер, навколишнього простору чи рухи шолома.</li>
</ul>
<p>Уся обробка відбувається на вашому комп'ютері. Відео передається з комп'ютера в шолом через вашу локальну мережу (Wi-Fi або кабель), не через інтернет.</p>
<h2>Що ми збираємо (анонімна статистика використання)</h2>
<p>Щоб знаходити проблеми й робити застосунок швидшим на більшій кількості комп'ютерів, застосунок для комп'ютера надсилає технічну інформацію, як-от:</p>
<ul>
<li>Випадковий код, створений під час встановлення, не пов'язаний із вами (потрібен лише для підрахунку встановлень без повторів).</li>
<li>Версію Pop3D і Windows, мову системи та застосунку.</li>
<li>Модель відеокарти, відеопам'ять, версію драйвера, процесор і оперативну пам'ять.</li>
<li>Показники продуктивності: кадри за секунду, навантаження на відеокарту й вибрану якість.</li>
<li>Як використовується застосунок: тип шолома та підключення (Wi-Fi, кабель, PC VR), режим відео (2D, 3D, екран ПК), час використання.</li>
<li>Етапи встановлення та повідомлення про помилки (без назв файлів чи папок). Коли стається помилка або відео зависає, разом надсилаються останні рядки технічного журналу застосунку, очищені ще до виходу з комп'ютера: без назв фільмів, файлів, папок, e-mail чи IP-адрес.</li>
</ul>
<p>Ці дані зберігає <b>PostHog</b>, сервіс статистики, на серверах у <b>Європейському Союзі</b>, і їх бачить лише команда Pop3D. Ми не продаємо й нікому не передаємо ці дані та не використовуємо їх для реклами.</p>
<h2>Пропозиції, які ви нам надсилаєте</h2>
<p>У розділі <b>Ідеї та пропозиції</b> в застосунку ви можете надіслати нам повідомлення. Разом із вашим текстом надсилаються версія застосунку та модель відеокарти. E-mail <b>необов'язковий</b>: він надсилається, лише якщо ви його вкажете, і використовується тільки для відповіді. Пропозиції зберігаються в тому самому сервісі, що й статистика (PostHog, Європейський Союз). Вони надсилаються навіть із вимкненою статистикою, бо надсилати їх вирішуєте ви.</p>
<h2>Як вимкнути</h2>
<p>У застосунку для комп'ютера відкрийте <b>Налаштування</b> й вимкніть <b>Надсилати анонімні дані про використання</b>. Відтоді більше нічого не надсилається (крім пропозицій, які ви вирішите надіслати).</p>
<h2>Оновлення</h2>
<p>Під час запуску Pop3D звертається до <b>GitHub</b> (де публікуються версії), щоб дізнатися, чи вийшла нова версія. Як і будь-який сайт, GitHub у цей момент отримує інтернет-адресу вашого комп'ютера; до цього запиту застосовується політика конфіденційності GitHub. Жодна інформація про вас разом не надсилається.</p>
<h2>Застосунок для шолома (Meta Quest)</h2>
<p>Застосунок Pop3D для шолома не збирає й не надсилає жодних даних в інтернет. Він спілкується лише з вашим комп'ютером у локальній мережі, щоб отримувати відео й надсилати команди контролерів.</p>
<h2>Діти</h2>
<p>Pop3D не збирає персональних даних нікого, зокрема дітей. Дотримуйтеся вікових рекомендацій виробника вашого шолома.</p>
<h2>Ваші права (GDPR і LGPD)</h2>
<p>Оскільки статистика анонімна, ми не можемо пов'язати її з вами. Проте, якщо ви хочете, щоб ми видалили статистику вашого комп'ютера або надіслану вами пропозицію, напишіть нам за посиланням нижче й укажіть код встановлення, який показано в Налаштуваннях.</p>
<h2>Зміни цієї політики</h2>
<p>Якщо ця політика зміниться, нова версія з'явиться на цій сторінці з оновленою датою.</p>
<h2>Контакти</h2>
<p>Питання чи запити: {ISSUES}.</p>
"""}

SV = {"titulo": "Integritetspolicy", "atualizada": "Uppdaterad", "inicio": "Startsida", "corpo": f"""
<div class="resumo"><p><b>I korthet:</b> dina filmer och videor lämnar aldrig din dator. Pop3D skickar bara anonym användningsstatistik (som grafikkortsmodell och prestanda) så att vi kan förbättra appen, och du kan stänga av det när som helst under Inställningar.</p></div>
<h2>Vilka vi är</h2>
<p>Pop3D är en gratis app som förvandlar 2D-videor till 3D för VR-headset. Den består av datorappen (Windows) och headsetappen (Meta Quest). Den här policyn gäller båda.</p>
<h2>Det här samlar vi aldrig in</h2>
<ul>
<li>Namn, innehåll eller bilder från dina filmer och videor, eller något som visas på din datorskärm.</li>
<li>Namn på mappar och filer på din dator.</li>
<li>Ditt namn, konton, kontakter eller andra uppgifter som identifierar dig (en e-postadress bara om du själv skriver den i ett förslag; se nedan).</li>
<li>Din IP-adress: den sparas inte och används inte för att ta reda på var du befinner dig.</li>
<li>Kamerabilder, din omgivning eller headsetets rörelser.</li>
</ul>
<p>All bearbetning sker på din egen dator. Videon går från datorn till headsetet via ditt lokala nätverk (wifi eller kabel), aldrig via internet.</p>
<h2>Det här samlar vi in (anonym användningsstatistik)</h2>
<p>För att hitta problem och göra appen snabbare på fler datorer skickar datorappen teknisk information som:</p>
<ul>
<li>En slumpmässig kod som skapas vid installationen och inte har något med dig att göra (används bara för att räkna installationer utan dubbletter).</li>
<li>Versioner av Pop3D och Windows, system- och appspråk.</li>
<li>Grafikkortsmodell, videominne, drivrutinsversion, processor och RAM.</li>
<li>Prestandaresultat: bilder per sekund, grafikkortets belastning och vald kvalitet.</li>
<li>Hur appen används: typ av headset och anslutning (wifi, kabel, PC VR), videoläge (2D, 3D, datorskärm), användningstid.</li>
<li>Installationssteg och felmeddelanden (utan fil- eller mappnamn). När ett fel inträffar eller videon fryser skickas de sista raderna i appens tekniska logg med, rensade innan de lämnar datorn: inga film-, fil- eller mappnamn, e-postadresser eller IP-adresser.</li>
</ul>
<p>Uppgifterna lagras av <b>PostHog</b>, en analystjänst, på servrar i <b>Europeiska unionen</b>, och ses bara av Pop3D-teamet. Vi säljer inte och delar inte uppgifterna med någon annan, och vi använder dem inte för reklam.</p>
<h2>Förslag som du skickar till oss</h2>
<p>Under <b>Idéer och feedback</b> i appen kan du skicka ett meddelande till oss. Tillsammans med texten du skriver skickas appversionen och din grafikkortsmodell. E-postadressen är <b>valfri</b>: den skickas bara om du fyller i den och används bara för att svara på ditt meddelande. Förslagen lagras i samma tjänst som statistiken (PostHog, Europeiska unionen). De skickas även när statistiken är avstängd, eftersom det är du som väljer att skicka dem.</p>
<h2>Så stänger du av det</h2>
<p>Öppna <b>Inställningar</b> i datorappen och stäng av <b>Skicka anonym användningsdata</b>. Därefter skickas inget mer (förutom förslag som du själv väljer att skicka).</p>
<h2>Uppdateringar</h2>
<p>När Pop3D startar kontrollerar det <b>GitHub</b> (där versionerna publiceras) för att se om en ny version har kommit. Som alla webbplatser får GitHub din dators internetadress i det ögonblicket; GitHubs integritetspolicy gäller för den kontrollen. Inga av dina uppgifter skickas med.</p>
<h2>Headsetappen (Meta Quest)</h2>
<p>Pop3D-appen i headsetet samlar inte in och skickar inte några uppgifter till internet. Den kommunicerar bara med din dator, i ditt lokala nätverk, för att ta emot video och skicka handkontrollernas kommandon.</p>
<h2>Barn</h2>
<p>Pop3D samlar inte in personuppgifter från någon, inte heller från barn. Följ headsettillverkarens åldersrekommendationer.</p>
<h2>Dina rättigheter (GDPR och LGPD)</h2>
<p>Eftersom statistiken är anonym kan vi inte koppla den till dig. Om du ändå vill att vi raderar statistiken från din dator eller ett förslag som du har skickat kan du kontakta oss via länken nedan och ange installationskoden som visas under Inställningar.</p>
<h2>Ändringar i den här policyn</h2>
<p>Om policyn ändras visas den nya versionen på den här sidan med ett uppdaterat datum.</p>
<h2>Kontakt</h2>
<p>Frågor eller önskemål: {ISSUES}.</p>
"""}

JA = {"titulo": "プライバシーポリシー", "atualizada": "更新日", "inicio": "ホーム", "corpo": f"""
<div class="resumo"><p><b>要約：</b>あなたの映画や動画がパソコンの外に出ることはありません。Pop3D が送るのは、アプリを改善するための匿名の利用統計（グラフィックボードの型番や性能など）だけで、設定からいつでもオフにできます。</p></div>
<h2>運営者について</h2>
<p>Pop3D は、2D 動画を VR ヘッドセット向けの 3D に変える無料アプリです。パソコン用アプリ（Windows）とヘッドセット用アプリ（Meta Quest）からなり、本ポリシーはその両方に適用されます。</p>
<h2>収集しないもの</h2>
<ul>
<li>映画や動画のタイトル、内容、映像、およびパソコンの画面に表示されるもの。</li>
<li>パソコン内のフォルダ名やファイル名。</li>
<li>お名前、アカウント、連絡先など、あなたを特定できる情報（メールアドレスは、ご自身で提案に書き込んだ場合のみ。下記参照）。</li>
<li>IP アドレス：保存せず、所在地の特定にも使いません。</li>
<li>カメラの映像、周囲の環境、ヘッドセットの動き。</li>
</ul>
<p>処理はすべてあなたのパソコンの中で行われます。映像はローカルネットワーク（Wi-Fi またはケーブル）を通ってパソコンからヘッドセットへ届き、インターネットを経由することはありません。</p>
<h2>収集するもの（匿名の利用統計）</h2>
<p>問題を見つけ、より多くのパソコンでアプリを速くするために、パソコン用アプリは次のような技術情報を送信します。</p>
<ul>
<li>インストール時に作られるランダムなコード。あなたとは無関係です（インストール数を重複なく数えるためだけに使います）。</li>
<li>Pop3D と Windows のバージョン、システムとアプリの言語。</li>
<li>グラフィックボードの型番、ビデオメモリ、ドライバーのバージョン、プロセッサー、メモリ（RAM）。</li>
<li>性能の結果：1 秒あたりのフレーム数、グラフィックボードの使用率、選ばれた画質。</li>
<li>アプリの使われ方：ヘッドセットと接続の種類（Wi-Fi、ケーブル、PC VR）、映像モード（2D、3D、パソコンの画面）、利用時間。</li>
<li>インストールの段階とエラーメッセージ（ファイル名やフォルダ名は含みません）。エラーや映像の停止が起きたときは、アプリの技術ログの最後の数行も送られますが、パソコンを出る前に整理され、映画名、ファイル名、フォルダ名、メールアドレス、IP アドレスは含まれません。</li>
</ul>
<p>これらのデータは分析サービス <b>PostHog</b> によって<b>欧州連合</b>内のサーバーに保存され、Pop3D チームだけが閲覧します。データを販売したり第三者と共有したりすることはなく、広告にも使いません。</p>
<h2>お寄せいただく提案</h2>
<p>アプリ内の <b>アイデアとご意見</b> からメッセージを送れます。書いた文章と一緒に、アプリのバージョンとグラフィックボードの型番が送られます。メールアドレスは<b>任意</b>で、入力した場合のみ送られ、返信のためだけに使います。提案は統計と同じサービス（PostHog、欧州連合）に保存されます。ご自身で送ると決めたものなので、統計をオフにしていても送信されます。</p>
<h2>オフにする方法</h2>
<p>パソコン用アプリで <b>設定</b> を開き、<b>匿名の使用データを送信</b> をオフにしてください。それ以降は何も送信されません（ご自身で送る提案を除きます）。</p>
<h2>アップデート</h2>
<p>Pop3D は起動時に <b>GitHub</b>（バージョンを公開している場所）を確認し、新しいバージョンが出ているかを調べます。ほかのウェブサイトと同じく、その際に GitHub はパソコンのインターネット上のアドレスを受け取ります。この確認には GitHub のプライバシーポリシーが適用されます。あなたの情報が一緒に送られることはありません。</p>
<h2>ヘッドセット用アプリ（Meta Quest）</h2>
<p>ヘッドセット用の Pop3D アプリは、データを収集したり、インターネットに送ったりしません。映像を受け取り、コントローラーの操作を送るために、ローカルネットワーク内であなたのパソコンとやり取りするだけです。</p>
<h2>お子さまについて</h2>
<p>Pop3D は、お子さまを含め、誰の個人データも収集しません。ヘッドセットのメーカーが定める対象年齢に従ってください。</p>
<h2>あなたの権利（GDPR・LGPD）</h2>
<p>統計は匿名のため、あなたと結びつけることはできません。それでも、お使いのパソコンの統計や、送った提案の削除をご希望の場合は、設定に表示されるインストールコードを添えて、下記のリンクからご連絡ください。</p>
<h2>本ポリシーの変更</h2>
<p>本ポリシーを変更した場合は、更新日とともにこのページに新しい内容を掲載します。</p>
<h2>お問い合わせ</h2>
<p>ご質問やご要望：{ISSUES}</p>
"""}

ZH = {"titulo": "隱私權政策", "atualizada": "更新日期", "inicio": "首頁", "corpo": f"""
<div class="resumo"><p><b>重點摘要：</b>你的電影和影片永遠不會離開你的電腦。Pop3D 只會傳送匿名的使用統計（例如顯示卡型號和效能），讓我們改進應用程式，你也可以隨時在 設定中關閉。</p></div>
<h2>關於我們</h2>
<p>Pop3D 是一款免費應用程式，能把 2D 影片轉成 VR 頭戴裝置用的 3D。它包含電腦應用程式（Windows）和頭戴裝置應用程式（Meta Quest），本政策適用於兩者。</p>
<h2>我們絕不收集的資料</h2>
<ul>
<li>你的電影和影片的名稱、內容或畫面，以及電腦螢幕上顯示的任何內容。</li>
<li>電腦中資料夾和檔案的名稱。</li>
<li>你的姓名、帳號、聯絡人或任何能識別你的資料（電子郵件地址只有在你自己填進建議時才會傳送，見下文）。</li>
<li>你的 IP 位址：不會被儲存，也不會用來找出你的所在位置。</li>
<li>攝影機畫面、你周圍的環境或頭戴裝置的動作。</li>
</ul>
<p>所有處理都在你自己的電腦上進行。影片透過你的區域網路（Wi-Fi 或線材）從電腦傳到頭戴裝置，絕不經過網際網路。</p>
<h2>我們收集的資料（匿名使用統計）</h2>
<p>為了找出問題，並讓應用程式在更多電腦上跑得更快，電腦應用程式會傳送以下技術資訊：</p>
<ul>
<li>安裝時產生的隨機代碼，與你本人無關（只用來計算安裝次數而不重複）。</li>
<li>Pop3D 與 Windows 的版本、系統與應用程式的語言。</li>
<li>顯示卡型號、顯示記憶體、驅動程式版本、處理器和記憶體（RAM）。</li>
<li>效能結果：每秒影格數、顯示卡使用率和所選的畫質。</li>
<li>應用程式的使用方式：頭戴裝置與連線類型（Wi-Fi、線材、PC VR）、影片模式（2D、3D、電腦螢幕）、使用時間。</li>
<li>安裝步驟和錯誤訊息（不含檔案或資料夾名稱）。發生錯誤或影片卡住時，會一併傳送應用程式技術記錄的最後幾行，並在離開電腦前先清理過：不含電影、檔案或資料夾名稱、電子郵件或 IP 位址。</li>
</ul>
<p>這些資料由分析服務 <b>PostHog</b> 儲存在<b>歐盟</b>境內的伺服器，只有 Pop3D 團隊能查看。我們不會出售或與任何人分享這些資料，也不會用於廣告。</p>
<h2>你傳給我們的建議</h2>
<p>在應用程式的 <b>點子與意見</b> 中，你可以傳訊息給我們。除了你寫的內容，還會附上應用程式版本和你的顯示卡型號。電子郵件是<b>選填</b>的：只有在你填寫時才會傳送，而且只用來回覆你的訊息。建議和統計資料存放在同一個服務（PostHog，歐盟）。即使關閉統計，建議仍會傳送，因為是你自己決定要傳的。</p>
<h2>如何關閉</h2>
<p>在電腦應用程式中打開 <b>設定</b>，關閉 <b>傳送匿名使用資料</b>。之後就不會再傳送任何資料（你自己選擇傳送的建議除外）。</p>
<h2>更新</h2>
<p>Pop3D 開啟時會查詢 <b>GitHub</b>（發布版本的地方），看看是否有新版本。就像任何網站一樣，GitHub 在那一刻會收到你電腦的網路位址；這項查詢適用 GitHub 的隱私權政策。不會附帶你的任何資訊。</p>
<h2>頭戴裝置應用程式（Meta Quest）</h2>
<p>頭戴裝置上的 Pop3D 應用程式不會收集資料，也不會傳送任何資料到網際網路。它只在你的區域網路中和你的電腦溝通，用來接收影片和傳送控制器的操作。</p>
<h2>兒童</h2>
<p>Pop3D 不會收集任何人的個人資料，包括兒童。請遵守頭戴裝置製造商的年齡建議。</p>
<h2>你的權利（GDPR 與 LGPD）</h2>
<p>由於統計資料是匿名的，我們無法把它和你連結起來。即使如此，如果你希望我們刪除你電腦的統計資料或你傳送的建議，請透過下方連結聯絡我們，並提供設定中顯示的安裝代碼。</p>
<h2>本政策的變更</h2>
<p>如果本政策有所變更，新版本會連同更新日期顯示在這個頁面。</p>
<h2>聯絡我們</h2>
<p>問題或要求：{ISSUES}。</p>
"""}

NL = {"titulo": "Privacybeleid", "atualizada": "Bijgewerkt op", "inicio": "Startpagina", "corpo": f"""
<div class="resumo"><p><b>In het kort:</b> je films en video's verlaten nooit je computer. Pop3D stuurt alleen anonieme gebruiksstatistieken (zoals het model van je videokaart en de prestaties) zodat we de app kunnen verbeteren, en je kunt dat op elk moment uitzetten in Instellingen.</p></div>
<h2>Wie we zijn</h2>
<p>Pop3D is een gratis app die 2D-video's omzet in 3D voor VR-headsets. Hij bestaat uit de computerapp (Windows) en de headsetapp (Meta Quest). Dit beleid geldt voor allebei.</p>
<h2>Wat we nooit verzamelen</h2>
<ul>
<li>Namen, inhoud of beelden van je films en video's, of wat er op je computerscherm staat.</li>
<li>Namen van mappen en bestanden op je computer.</li>
<li>Je naam, accounts, contacten of andere gegevens die jou identificeren (een e-mailadres alleen als je het zelf in een suggestie typt; zie hieronder).</li>
<li>Je IP-adres: het wordt niet opgeslagen en niet gebruikt om te achterhalen waar je bent.</li>
<li>Camerabeelden, je omgeving of de bewegingen van de headset.</li>
</ul>
<p>Alle verwerking gebeurt op je eigen computer. De video gaat via je lokale netwerk (wifi of kabel) van je computer naar je headset, nooit via internet.</p>
<h2>Wat we verzamelen (anonieme gebruiksstatistieken)</h2>
<p>Om problemen te vinden en de app op meer computers sneller te maken, stuurt de computerapp technische informatie zoals:</p>
<ul>
<li>Een willekeurige code die bij de installatie wordt aangemaakt en niets met jou te maken heeft (alleen gebruikt om installaties zonder dubbeltellingen te tellen).</li>
<li>Versies van Pop3D en Windows, taal van het systeem en van de app.</li>
<li>Model van de videokaart, videogeheugen, driverversie, processor en RAM.</li>
<li>Prestatieresultaten: beelden per seconde, gebruik van de videokaart en de gekozen kwaliteit.</li>
<li>Hoe de app wordt gebruikt: headset en type verbinding (wifi, kabel, pc-VR), videomodus (2D, 3D, pc-scherm), gebruikstijd.</li>
<li>Installatiestappen en foutmeldingen (zonder namen van bestanden of mappen). Als er een fout optreedt of de video vastloopt, gaan de laatste regels van het technische logboek van de app mee, opgeschoond voordat ze de computer verlaten: geen namen van films, bestanden of mappen, geen e-mailadressen of IP-adressen.</li>
</ul>
<p>Deze gegevens worden opgeslagen door <b>PostHog</b>, een analysedienst, op servers in de <b>Europese Unie</b>, en zijn alleen zichtbaar voor het Pop3D-team. We verkopen of delen deze gegevens met niemand anders en gebruiken ze niet voor advertenties.</p>
<h2>Suggesties die je ons stuurt</h2>
<p>Onder <b>Ideeën en feedback</b> in de app kun je ons een bericht sturen. Samen met de tekst die je schrijft worden de appversie en het model van je videokaart verstuurd. Je e-mailadres is <b>optioneel</b>: het wordt alleen verstuurd als je het invult en wordt alleen gebruikt om op je bericht te antwoorden. Suggesties worden opgeslagen in dezelfde dienst als de statistieken (PostHog, Europese Unie). Ze worden ook verstuurd als de statistieken uit staan, omdat jij ervoor kiest ze te sturen.</p>
<h2>Zo zet je het uit</h2>
<p>Open in de computerapp <b>Instellingen</b> en zet <b>Anonieme gebruiksgegevens versturen</b> uit. Vanaf dat moment wordt er niets meer verstuurd (behalve suggesties die je zelf kiest te sturen).</p>
<h2>Updates</h2>
<p>Bij het openen controleert Pop3D op <b>GitHub</b> (waar de versies worden gepubliceerd) of er een nieuwe versie is. Zoals bij elke website ontvangt GitHub op dat moment het internetadres van je computer; op die controle is het privacybeleid van GitHub van toepassing. Er worden geen gegevens van jou meegestuurd.</p>
<h2>Headsetapp (Meta Quest)</h2>
<p>De Pop3D-headsetapp verzamelt geen gegevens en stuurt niets naar internet. Hij praat alleen met je computer, op je lokale netwerk, om video te ontvangen en de invoer van de controllers te versturen.</p>
<h2>Kinderen</h2>
<p>Pop3D verzamelt van niemand persoonsgegevens, ook niet van kinderen. Volg de leeftijdsaanbevelingen van de fabrikant van je headset.</p>
<h2>Je rechten (AVG en LGPD)</h2>
<p>Omdat de statistieken anoniem zijn, kunnen we ze niet aan jou koppelen. Wil je toch dat we de statistieken van je computer of een suggestie die je hebt gestuurd verwijderen, neem dan contact met ons op via de link hieronder en vermeld de installatiecode die in Instellingen staat.</p>
<h2>Wijzigingen in dit beleid</h2>
<p>Als dit beleid verandert, verschijnt de nieuwe versie op deze pagina met een bijgewerkte datum.</p>
<h2>Contact</h2>
<p>Vragen of verzoeken: {ISSUES}.</p>
"""}

HU = {"titulo": "Adatvédelmi irányelvek", "atualizada": "Frissítve:", "inicio": "Kezdőlap", "corpo": f"""
<div class="resumo"><p><b>Röviden:</b> a filmjeid és videóid soha nem hagyják el a számítógépedet. A Pop3D csak névtelen használati statisztikákat küld (például a videokártya típusát és a teljesítményt), hogy javíthassuk az alkalmazást, és ezt bármikor kikapcsolhatod a Beállításokban.</p></div>
<h2>Kik vagyunk</h2>
<p>A Pop3D egy ingyenes alkalmazás, amely a 2D-s videókat 3D-vé alakítja VR-headsetekhez. A számítógépes alkalmazásból (Windows) és a headsetalkalmazásból (Meta Quest) áll. Ezek az irányelvek mindkettőre vonatkoznak.</p>
<h2>Amit soha nem gyűjtünk</h2>
<ul>
<li>A filmjeid és videóid nevét, tartalmát vagy képeit, sem azt, ami a számítógéped képernyőjén látszik.</li>
<li>A számítógépeden lévő mappák és fájlok nevét.</li>
<li>A nevedet, fiókjaidat, névjegyeidet vagy bármilyen adatot, amely azonosít téged (e-mail-címet csak akkor, ha te magad írod be egy javaslatba; lásd lent).</li>
<li>Az IP-címedet: nem tároljuk, és nem használjuk arra, hogy kiderítsük, hol vagy.</li>
<li>Kameraképeket, a környezetedet vagy a headset mozgását.</li>
</ul>
<p>Minden feldolgozás a saját számítógépeden történik. A videó a helyi hálózaton (wifin vagy kábelen) jut el a számítógépedről a headsetedbe, soha nem az interneten át.</p>
<h2>Amit gyűjtünk (névtelen használati statisztikák)</h2>
<p>Hogy megtaláljuk a hibákat, és több gépen gyorsabbá tegyük az alkalmazást, a számítógépes alkalmazás ilyen technikai adatokat küld:</p>
<ul>
<li>Egy véletlenszerű kódot, amely a telepítéskor jön létre, és semmi köze hozzád (csak arra szolgál, hogy ismétlődés nélkül számoljuk a telepítéseket).</li>
<li>A Pop3D és a Windows verzióját, a rendszer és az alkalmazás nyelvét.</li>
<li>A videokártya típusát, a videomemóriát, az illesztőprogram verzióját, a processzort és a RAM-ot.</li>
<li>Teljesítményadatokat: képkocka per másodperc, a videokártya kihasználtsága és a választott minőség.</li>
<li>Az alkalmazás használatát: a headsetet és a kapcsolat típusát (wifi, kábel, PC-s VR), a videómódot (2D, 3D, PC-képernyő), a használati időt.</li>
<li>A telepítés lépéseit és a hibaüzeneteket (fájl- és mappanevek nélkül). Ha hiba történik vagy a videó megakad, az alkalmazás technikai naplójának utolsó sorai is mennek, megtisztítva, mielőtt elhagyják a gépet: filmek, fájlok és mappák neve, e-mail- és IP-címek nélkül.</li>
</ul>
<p>Ezeket az adatokat a <b>PostHog</b> nevű elemzőszolgáltatás tárolja az <b>Európai Unióban</b> lévő szervereken, és csak a Pop3D csapata látja őket. Az adatokat nem adjuk el, nem osztjuk meg senki mással, és nem használjuk reklámra.</p>
<h2>Javaslatok, amelyeket küldesz nekünk</h2>
<p>Az alkalmazás <b>Ötletek és visszajelzés</b> részében üzenetet küldhetsz nekünk. Az általad írt szöveggel együtt elküldjük az alkalmazás verzióját és a videokártyád típusát. Az e-mail-cím <b>nem kötelező</b>: csak akkor küldjük el, ha kitöltöd, és csak arra használjuk, hogy válaszoljunk az üzenetedre. A javaslatokat ugyanabban a szolgáltatásban tároljuk, mint a statisztikákat (PostHog, Európai Unió). Kikapcsolt statisztikák mellett is elküldjük őket, mert te döntesz úgy, hogy elküldöd.</p>
<h2>Hogyan kapcsolhatod ki</h2>
<p>A számítógépes alkalmazásban nyisd meg a <b>Beállítások</b> menüt, és kapcsold ki a <b>Névtelen használati adatok küldése</b> lehetőséget. Ettől kezdve semmi más nem megy el (kivéve a javaslatokat, amelyeket te magad küldesz).</p>
<h2>Frissítések</h2>
<p>Megnyitáskor a Pop3D megnézi a <b>GitHubon</b> (ahol a verziók megjelennek), hogy van-e új verzió. Mint bármely weboldal, a GitHub ekkor megkapja a számítógéped internetcímét; erre az ellenőrzésre a GitHub adatvédelmi irányelvei vonatkoznak. Rólad semmilyen adat nem megy vele.</p>
<h2>Headsetalkalmazás (Meta Quest)</h2>
<p>A Pop3D headsetalkalmazása nem gyűjt adatot, és semmit nem küld az internetre. Csak a számítógépeddel kommunikál a helyi hálózaton, hogy fogadja a videót és elküldje a kontrollerek jeleit.</p>
<h2>Gyermekek</h2>
<p>A Pop3D senkitől sem gyűjt személyes adatot, gyermekektől sem. Kövesd a headset gyártójának életkorra vonatkozó ajánlásait.</p>
<h2>A jogaid (GDPR és LGPD)</h2>
<p>Mivel a statisztikák névtelenek, nem tudjuk őket hozzád kapcsolni. Ha mégis szeretnéd, hogy töröljük a számítógéped statisztikáit vagy egy általad küldött javaslatot, írj nekünk az alábbi linken, és add meg a Beállításokban látható telepítési kódot.</p>
<h2>Az irányelvek változásai</h2>
<p>Ha az irányelvek megváltoznak, az új változat ezen az oldalon jelenik meg, frissített dátummal.</p>
<h2>Kapcsolat</h2>
<p>Kérdések vagy kérések: {ISSUES}.</p>
"""}

RU = {"titulo": "Политика конфиденциальности", "atualizada": "Обновлено", "inicio": "Главная", "corpo": f"""
<div class="resumo"><p><b>Коротко:</b> ваши фильмы и видео никогда не покидают компьютер. Pop3D отправляет только анонимную статистику использования (например, модель видеокарты и производительность), чтобы мы могли улучшать приложение, и это можно отключить в любой момент в Настройках.</p></div>
<h2>Кто мы</h2>
<p>Pop3D — бесплатное приложение, которое превращает 2D-видео в 3D для VR-шлемов. Оно состоит из приложения для компьютера (Windows) и приложения для шлема (Meta Quest). Эта политика распространяется на оба.</p>
<h2>Что мы никогда не собираем</h2>
<ul>
<li>Названия, содержимое или кадры ваших фильмов и видео, а также то, что показывается на экране компьютера.</li>
<li>Названия папок и файлов на вашем компьютере.</li>
<li>Ваше имя, аккаунты, контакты и любые данные, по которым можно вас узнать (адрес электронной почты — только если вы сами укажете его в предложении; см. ниже).</li>
<li>Ваш IP-адрес: он не сохраняется и не используется, чтобы узнать, где вы находитесь.</li>
<li>Изображения с камер, ваше окружение или движения шлема.</li>
</ul>
<p>Вся обработка происходит на вашем компьютере. Видео идёт с компьютера в шлем по локальной сети (Wi-Fi или кабель), а не через интернет.</p>
<h2>Что мы собираем (анонимная статистика использования)</h2>
<p>Чтобы находить проблемы и ускорять приложение на большем числе компьютеров, приложение для компьютера отправляет техническую информацию, например:</p>
<ul>
<li>Случайный код, созданный при установке и никак с вами не связанный (нужен только для подсчёта установок без повторов).</li>
<li>Версии Pop3D и Windows, язык системы и приложения.</li>
<li>Модель видеокарты, объём видеопамяти, версию драйвера, процессор и ОЗУ.</li>
<li>Показатели производительности: кадры в секунду, загрузку видеокарты и выбранное качество.</li>
<li>Как используется приложение: шлем и тип подключения (Wi-Fi, кабель, ПК VR), режим видео (2D, 3D, экран ПК), время использования.</li>
<li>Шаги установки и сообщения об ошибках (без названий файлов и папок). Если возникает ошибка или видео зависает, вместе с ними отправляются последние строки технического журнала приложения, очищенные ещё до отправки: без названий фильмов, файлов и папок, адресов электронной почты и IP-адресов.</li>
</ul>
<p>Эти данные хранит аналитический сервис <b>PostHog</b> на серверах в <b>Европейском союзе</b>, и видит их только команда Pop3D. Мы не продаём эти данные, никому их не передаём и не используем для рекламы.</p>
<h2>Предложения, которые вы нам присылаете</h2>
<p>В разделе <b>Идеи и отзывы</b> в приложении можно отправить нам сообщение. Вместе с вашим текстом отправляются версия приложения и модель видеокарты. Адрес электронной почты <b>указывать не обязательно</b>: он отправляется, только если вы его заполните, и используется только для ответа на ваше сообщение. Предложения хранятся в том же сервисе, что и статистика (PostHog, Европейский союз). Они отправляются даже при отключённой статистике, потому что вы сами решаете их отправить.</p>
<h2>Как это отключить</h2>
<p>В приложении для компьютера откройте <b>Настройки</b> и отключите <b>Отправлять анонимные данные об использовании</b>. После этого ничего больше не отправляется (кроме предложений, которые вы решите отправить сами).</p>
<h2>Обновления</h2>
<p>При запуске Pop3D проверяет на <b>GitHub</b> (где публикуются версии), не вышла ли новая версия. Как и любой сайт, GitHub в этот момент получает интернет-адрес вашего компьютера; к этой проверке применяется политика конфиденциальности GitHub. Никакие ваши данные при этом не отправляются.</p>
<h2>Приложение для шлема (Meta Quest)</h2>
<p>Приложение Pop3D для шлема не собирает данные и ничего не отправляет в интернет. Оно общается только с вашим компьютером в локальной сети, чтобы получать видео и передавать нажатия контроллеров.</p>
<h2>Дети</h2>
<p>Pop3D не собирает персональные данные ни у кого, в том числе у детей. Соблюдайте возрастные рекомендации производителя шлема.</p>
<h2>Ваши права (GDPR и LGPD)</h2>
<p>Поскольку статистика анонимна, мы не можем связать её с вами. Если вы всё же хотите, чтобы мы удалили статистику вашего компьютера или отправленное вами предложение, напишите нам по ссылке ниже и укажите код установки, который показан в Настройках.</p>
<h2>Изменения этой политики</h2>
<p>Если политика изменится, новая версия появится на этой странице с обновлённой датой.</p>
<h2>Контакты</h2>
<p>Вопросы и запросы: {ISSUES}.</p>
"""}

KO = {"titulo": "개인정보 처리방침", "atualizada": "업데이트:", "inicio": "홈", "corpo": f"""
<div class="resumo"><p><b>요약:</b> 영화와 영상은 절대 컴퓨터 밖으로 나가지 않습니다. Pop3D는 앱을 개선하기 위해 익명 사용 통계(그래픽 카드 모델, 성능 등)만 보내며, 언제든지 설정에서 끌 수 있습니다.</p></div>
<h2>운영자 소개</h2>
<p>Pop3D는 2D 영상을 VR 헤드셋용 3D로 바꿔 주는 무료 앱입니다. 컴퓨터 앱(Windows)과 헤드셋 앱(Meta Quest)으로 이루어져 있으며, 이 방침은 두 앱 모두에 적용됩니다.</p>
<h2>절대 수집하지 않는 정보</h2>
<ul>
<li>영화와 영상의 이름, 내용, 이미지, 그리고 컴퓨터 화면에 표시되는 내용.</li>
<li>컴퓨터에 있는 폴더와 파일의 이름.</li>
<li>이름, 계정, 연락처 등 사용자를 식별할 수 있는 모든 정보(이메일 주소는 사용자가 직접 제안에 입력한 경우에만 해당. 아래 참고).</li>
<li>IP 주소: 저장하지 않으며 위치를 알아내는 데 쓰지 않습니다.</li>
<li>카메라 이미지, 주변 환경, 헤드셋의 움직임.</li>
</ul>
<p>모든 처리는 사용자의 컴퓨터에서 이루어집니다. 영상은 로컬 네트워크(Wi-Fi 또는 케이블)를 통해 컴퓨터에서 헤드셋으로 전달되며, 인터넷을 거치지 않습니다.</p>
<h2>수집하는 정보(익명 사용 통계)</h2>
<p>문제를 찾고 더 많은 컴퓨터에서 앱을 더 빠르게 만들기 위해, 컴퓨터 앱은 다음과 같은 기술 정보를 보냅니다.</p>
<ul>
<li>설치 시 만들어지는 무작위 코드로, 사용자와는 아무 관련이 없습니다(설치 수를 중복 없이 세는 데만 사용).</li>
<li>Pop3D와 Windows 버전, 시스템과 앱의 언어.</li>
<li>그래픽 카드 모델, 비디오 메모리, 드라이버 버전, 프로세서, RAM.</li>
<li>성능 결과: 초당 프레임 수, 그래픽 카드 사용률, 선택한 화질.</li>
<li>앱 사용 방식: 헤드셋과 연결 방식(Wi-Fi, 케이블, PC VR), 영상 모드(2D, 3D, PC 화면), 사용 시간.</li>
<li>설치 단계와 오류 메시지(파일·폴더 이름 제외). 오류가 나거나 영상이 멈추면 앱 기술 로그의 마지막 몇 줄도 함께 보내며, 컴퓨터를 떠나기 전에 정리됩니다. 영화·파일·폴더 이름, 이메일 주소, IP 주소는 포함되지 않습니다.</li>
</ul>
<p>이 정보는 분석 서비스 <b>PostHog</b>가 <b>유럽연합</b> 내 서버에 저장하며, Pop3D 팀만 볼 수 있습니다. 이 정보를 판매하거나 다른 누구와도 공유하지 않으며, 광고에 사용하지 않습니다.</p>
<h2>보내 주신 제안</h2>
<p>앱의 <b>아이디어와 의견</b>에서 메시지를 보낼 수 있습니다. 작성한 내용과 함께 앱 버전과 그래픽 카드 모델이 전송됩니다. 이메일은 <b>선택 사항</b>이며, 입력한 경우에만 전송되고 메시지에 답장하는 데만 사용됩니다. 제안은 통계와 같은 서비스(PostHog, 유럽연합)에 저장됩니다. 사용자가 직접 보내기로 한 것이므로 통계를 꺼 두어도 전송됩니다.</p>
<h2>끄는 방법</h2>
<p>컴퓨터 앱에서 <b>설정</b>을 열고 <b>익명 사용 데이터 보내기</b>를 끄세요. 그 이후로는 아무것도 전송되지 않습니다(직접 보내기로 한 제안 제외).</p>
<h2>업데이트</h2>
<p>Pop3D는 실행될 때 <b>GitHub</b>(버전이 게시되는 곳)에서 새 버전이 나왔는지 확인합니다. 다른 웹사이트와 마찬가지로 이때 GitHub는 컴퓨터의 인터넷 주소를 받게 되며, 이 확인에는 GitHub의 개인정보 처리방침이 적용됩니다. 사용자의 정보는 함께 전송되지 않습니다.</p>
<h2>헤드셋 앱(Meta Quest)</h2>
<p>Pop3D 헤드셋 앱은 어떤 정보도 수집하지 않으며 인터넷으로 아무것도 보내지 않습니다. 영상을 받고 컨트롤러 입력을 보내기 위해 로컬 네트워크에서 컴퓨터와만 통신합니다.</p>
<h2>아동</h2>
<p>Pop3D는 아동을 포함해 누구의 개인정보도 수집하지 않습니다. 헤드셋 제조사의 권장 연령을 따라 주세요.</p>
<h2>사용자의 권리(GDPR 및 LGPD)</h2>
<p>통계는 익명이므로 사용자와 연결할 수 없습니다. 그래도 컴퓨터의 통계나 보낸 제안의 삭제를 원하시면, 설정에 표시되는 설치 코드를 적어 아래 링크로 연락해 주세요.</p>
<h2>방침 변경</h2>
<p>이 방침이 바뀌면 업데이트 날짜와 함께 새 버전이 이 페이지에 게시됩니다.</p>
<h2>문의</h2>
<p>질문이나 요청: {ISSUES}.</p>
"""}

ZH_HANS = {"titulo": "隐私政策", "atualizada": "更新日期", "inicio": "首页", "corpo": f"""
<div class="resumo"><p><b>摘要：</b>你的电影和视频永远不会离开你的电脑。Pop3D 只会发送匿名的使用统计（例如显卡型号和性能），帮助我们改进应用，你也可以随时在设置中关闭。</p></div>
<h2>关于我们</h2>
<p>Pop3D 是一款免费应用，能把 2D 视频转成 VR 头显用的 3D。它包括电脑应用（Windows）和头显应用（Meta Quest），本政策适用于两者。</p>
<h2>我们绝不收集的信息</h2>
<ul>
<li>你的电影和视频的名称、内容或画面，以及电脑屏幕上显示的任何内容。</li>
<li>你电脑上的文件夹和文件名称。</li>
<li>你的姓名、账号、联系人或任何能识别你的信息（电子邮件地址仅在你自己写进建议时才会发送；见下文）。</li>
<li>你的 IP 地址：不会被保存，也不会用来判断你在哪里。</li>
<li>摄像头画面、你周围的环境或头显的动作。</li>
</ul>
<p>所有处理都在你自己的电脑上完成。视频通过局域网（Wi-Fi 或数据线）从电脑传到头显，绝不经过互联网。</p>
<h2>我们收集的信息（匿名使用统计）</h2>
<p>为了发现问题，并让应用在更多电脑上运行得更快，电脑应用会发送以下技术信息：</p>
<ul>
<li>安装时生成的随机代码，与你本人无关（仅用于统计安装数量，避免重复）。</li>
<li>Pop3D 和 Windows 的版本，系统和应用的语言。</li>
<li>显卡型号、显存、驱动版本、处理器和内存。</li>
<li>性能结果：每秒帧数、显卡占用率和所选画质。</li>
<li>应用的使用方式：头显和连接方式（Wi-Fi、数据线、PC VR）、视频模式（2D、3D、电脑屏幕）、使用时长。</li>
<li>安装步骤和错误信息（不含文件或文件夹名称）。发生错误或视频卡住时，会一并发送应用技术日志的最后几行，并在离开电脑前清理：不含电影、文件或文件夹名称，也不含电子邮件地址或 IP 地址。</li>
</ul>
<p>这些数据由分析服务 <b>PostHog</b> 存储在<b>欧盟</b>境内的服务器上，只有 Pop3D 团队可以查看。我们不会出售或与任何人分享这些数据，也不会用于广告。</p>
<h2>你发给我们的建议</h2>
<p>在应用的 <b>想法与反馈</b> 中，你可以给我们发消息。除了你写的内容，还会附上应用版本和你的显卡型号。电子邮件是<b>选填</b>的：只有在你填写时才会发送，而且只用于回复你的消息。建议与统计数据存放在同一服务中（PostHog，欧盟）。即使关闭了统计，建议仍会发送，因为是你自己决定要发的。</p>
<h2>如何关闭</h2>
<p>在电脑应用中打开 <b>设置</b>，关闭 <b>发送匿名使用数据</b>。之后就不会再发送任何数据（你自己选择发送的建议除外）。</p>
<h2>更新</h2>
<p>Pop3D 打开时会访问 <b>GitHub</b>（发布版本的地方），查看是否有新版本。和任何网站一样，GitHub 在那一刻会收到你电脑的网络地址；这项检查适用 GitHub 的隐私政策。不会附带你的任何信息。</p>
<h2>头显应用（Meta Quest）</h2>
<p>Pop3D 头显应用不收集任何数据，也不会向互联网发送任何内容。它只在局域网中与你的电脑通信，用来接收视频并发送手柄操作。</p>
<h2>儿童</h2>
<p>Pop3D 不会收集任何人的个人信息，包括儿童。请遵守头显制造商的年龄建议。</p>
<h2>你的权利（GDPR 与 LGPD）</h2>
<p>由于统计数据是匿名的，我们无法把它与你联系起来。即便如此，如果你希望我们删除你电脑的统计数据或你发送的建议，请通过下方链接联系我们，并提供设置中显示的安装代码。</p>
<h2>本政策的变更</h2>
<p>如果本政策有变更，新版本会连同更新日期显示在本页面。</p>
<h2>联系我们</h2>
<p>问题或请求：{ISSUES}。</p>
"""}

IDIOMAS = {"pt": PT, "en": EN, "es": ES, "fr": FR, "de": DE, "it": IT, "uk": UK, "sv": SV, "ja": JA, "zh": ZH,
           "nl": NL, "hu": HU, "ru": RU, "ko": KO, "zh-hans": ZH_HANS}
