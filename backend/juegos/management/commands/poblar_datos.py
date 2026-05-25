from django.core.management.base import BaseCommand
from juegos.models import Genero, Plataforma, Juego, Noticia


class Command(BaseCommand):
    help = 'Puebla la base de datos con los juegos del catálogo Gamekey'

    def handle(self, *args, **kwargs):
        if Juego.objects.exists():
            self.stdout.write(self.style.WARNING('La base de datos ya tiene juegos. Abortando.'))
            return

        accion       = Genero.objects.get(nombre='Acción')
        rpg          = Genero.objects.get(nombre='RPG')
        terror       = Genero.objects.get(nombre='Terror')
        metroidvania = Genero.objects.get(nombre='Metroidvania')
        lucha        = Genero.objects.get(nombre='Lucha')
        roguelike    = Genero.objects.get(nombre='Roguelike')
        supervivencia = Genero.objects.get(nombre='Supervivencia')
        fps          = Genero.objects.get(nombre='FPS')

        pc    = Plataforma.objects.get(nombre='PC')
        ps5   = Plataforma.objects.get(nombre='PS5')
        switch = Plataforma.objects.get(nombre='Nintendo Switch')
        xbox  = Plataforma.objects.get(nombre='Xbox Series X')

        juegos = [
            dict(
                titulo='Devil May Cry 5',
                descripcion='Devil May Cry 5 es un videojuego de acción hack and slash desarrollado por Capcom. '
                            'Lanzado en 2019, el juego sigue a tres protagonistas —Nero, Dante y V— en su batalla '
                            'contra el rey demonio Urizen en la ciudad de Red Grave.',
                precio='19.99', precio_original='39.99',
                imagen='dmc.PNG', fecha_lanzamiento='2019-03-08', stock=120,
                genero=accion, plataforma=pc,
                destacado=True, top_ventas=True, novedad=False, en_descuento=True,
            ),
            dict(
                titulo='Devil May Cry 5: Special Edition',
                descripcion='Versión ampliada de DMC5 que incluye a Vergil como personaje jugable, '
                            'junto a mejoras visuales como ray tracing y la posibilidad de jugar a '
                            '120 fps. También incluye el modo Legendary Dark Knight con hordas masivas de enemigos.',
                precio='29.99', precio_original=None,
                imagen='vergil.jpg', fecha_lanzamiento='2020-11-10', stock=80,
                genero=accion, plataforma=ps5,
                destacado=False, top_ventas=False, novedad=False, en_descuento=False,
            ),
            dict(
                titulo='Devil May Cry HD Collection',
                descripcion='Recopilación remasterizada de los tres primeros Devil May Cry en alta definición. '
                            'Incluye DMC1, DMC2 y DMC3: Special Edition, con mejoras de resolución y rendimiento '
                            'respecto a los originales de PlayStation 2.',
                precio='14.99', precio_original='29.99',
                imagen='dmcHD.jpg', fecha_lanzamiento='2018-03-13', stock=60,
                genero=accion, plataforma=pc,
                destacado=False, top_ventas=False, novedad=False, en_descuento=True,
            ),
            dict(
                titulo='Sekiro: Shadows Die Twice',
                descripcion='Sekiro es un juego de acción y aventura de FromSoftware ambientado en el Japón '
                            'feudal del periodo Sengoku. El jugador encarna a Wolf, un shinobi que debe rescatar '
                            'a su señor y vengarse de un poderoso samurái. Ganador del GOTY 2019.',
                precio='34.99', precio_original='59.99',
                imagen='sekiro.jpg', fecha_lanzamiento='2019-03-22', stock=90,
                genero=accion, plataforma=pc,
                destacado=True, top_ventas=True, novedad=False, en_descuento=True,
            ),
            dict(
                titulo='Persona 3 Reload',
                descripcion='Remake completo de Persona 3 con gráficos modernos, nuevas escenas animadas y '
                            'contenido adicional. Sigue a un estudiante que descubre el poder de invocar Personas '
                            'para combatir criaturas que aparecen durante la Hora Oscura.',
                precio='49.99', precio_original=None,
                imagen='p3.avif', fecha_lanzamiento='2024-02-02', stock=70,
                genero=rpg, plataforma=pc,
                destacado=False, top_ventas=False, novedad=True, en_descuento=False,
            ),
            dict(
                titulo='Hollow Knight',
                descripcion='Hollow Knight es un juego de acción y aventura metroidvania de Team Cherry. '
                            'Explora el antiguo reino de Hallownest, un vasto mundo subterráneo lleno de insectos, '
                            'peligros y secretos. Aclamado por la crítica por su diseño artístico y jugabilidad.',
                precio='14.99', precio_original='14.99',
                imagen='Hollow.jpg', fecha_lanzamiento='2017-02-24', stock=300,
                genero=metroidvania, plataforma=pc,
                destacado=False, top_ventas=True, novedad=False, en_descuento=False,
            ),
            dict(
                titulo='Hollow Knight: Silksong',
                descripcion='Secuela de Hollow Knight en la que Hornet es la protagonista. '
                            'Explora un reino completamente nuevo lleno de criaturas, personajes y '
                            'jefes. Amplía la jugabilidad de su predecesor con nuevas mecánicas de combate.',
                precio='19.99', precio_original=None,
                imagen='silksong.avif', fecha_lanzamiento='2025-06-10', stock=200,
                genero=metroidvania, plataforma=pc,
                destacado=False, top_ventas=False, novedad=True, en_descuento=False,
            ),
            dict(
                titulo='Lies of P',
                descripcion='Lies of P es un soulslike que reimagina el cuento de Pinocho en la oscura ciudad '
                            'de Krat durante la Belle Époque. El jugador controla a P, una marioneta que busca '
                            'a su creador mientras combate contra autómatas enloquecidos.',
                precio='44.99', precio_original='59.99',
                imagen='liesofp.jpg', fecha_lanzamiento='2023-09-19', stock=85,
                genero=accion, plataforma=pc,
                destacado=False, top_ventas=False, novedad=True, en_descuento=True,
            ),
            dict(
                titulo='Hades',
                descripcion='Hades es un roguelike de acción de Supergiant Games en el que controlas a Zagreus, '
                            'hijo inmortal del dios del Inframundo, intentando escapar del reino de los muertos. '
                            'Combina una narrativa profunda con una jugabilidad frenética y altamente rejugable.',
                precio='24.99', precio_original=None,
                imagen='hades.jpg', fecha_lanzamiento='2020-09-17', stock=350,
                genero=roguelike, plataforma=pc,
                destacado=True, top_ventas=True, novedad=False, en_descuento=False,
            ),
            dict(
                titulo='Metal Gear Rising: Revengeance',
                descripcion='Metal Gear Rising es un juego de acción hack and slash desarrollado por PlatinumGames. '
                            'El protagonista es Raiden, un cyborg que trabaja para la PMC Maverick. '
                            'Destaca por su sistema de corte libre que permite dividir a los enemigos en partes.',
                precio='9.99', precio_original='19.99',
                imagen='mgr.jpg', fecha_lanzamiento='2014-01-09', stock=180,
                genero=accion, plataforma=pc,
                destacado=False, top_ventas=True, novedad=False, en_descuento=True,
            ),
            dict(
                titulo='Blasphemous',
                descripcion='Blasphemous es un hack and slash metroidvania de The Game Kitchen ambientado en Cvstodia, '
                            'un mundo oscuro y grotesco inspirado en el folclore y la iconografía religiosa española. '
                            'El jugador encarna al Penitente, único superviviente de la Masacre Silenciosa.',
                precio='17.99', precio_original='24.99',
                imagen='blasphemous.jpg', fecha_lanzamiento='2019-09-10', stock=110,
                genero=metroidvania, plataforma=pc,
                destacado=False, top_ventas=False, novedad=False, en_descuento=True,
            ),
            dict(
                titulo='Persona 5 Royal',
                descripcion='Persona 5 Royal es la versión definitiva de Persona 5, un JRPG de Atlus. '
                            'El jugador lidera a los Phantom Thieves, un grupo de estudiantes que entran '
                            'en el Palacio mental de adultos corruptos para robarles el corazón.',
                precio='39.99', precio_original=None,
                imagen='p5.jpg', fecha_lanzamiento='2022-10-21', stock=130,
                genero=rpg, plataforma=pc,
                destacado=True, top_ventas=True, novedad=False, en_descuento=False,
            ),
            dict(
                titulo='The Coma 2: Vicious Sisters',
                descripcion='The Coma 2 es una aventura de terror coreana de Devespresso Games. '
                            'Mina, una estudiante, despierta en una versión distorsionada y aterradora de '
                            'su colegio y debe sobrevivir a la noche mientras resuelve el misterio que la rodea.',
                precio='14.99', precio_original='19.99',
                imagen='thecoma2.jpg', fecha_lanzamiento='2020-01-28', stock=45,
                genero=terror, plataforma=pc,
                destacado=False, top_ventas=False, novedad=False, en_descuento=True,
            ),
            dict(
                titulo='The Elder Scrolls V: Skyrim',
                descripcion='Skyrim es un RPG de mundo abierto de Bethesda en el que el jugador encarna al '
                            'Dovahkiin, un cazador de dragones. Con más de diez años de vida, sigue siendo '
                            'uno de los juegos de rol más vendidos de la historia.',
                precio='9.99', precio_original='39.99',
                imagen='skyrim.jpg', fecha_lanzamiento='2011-11-11', stock=600,
                genero=rpg, plataforma=pc,
                destacado=False, top_ventas=True, novedad=False, en_descuento=True,
            ),
            dict(
                titulo='Dying Light 2: Stay Human',
                descripcion='Dying Light 2 es un juego de mundo abierto en primera persona de Techland. '
                            'Ambientado en la ciudad de Villedor, el jugador debe sobrevivir a una epidemia '
                            'zombi mientras las decisiones que tome moldean el destino de la ciudad.',
                precio='29.99', precio_original='49.99',
                imagen='dyinglight2.jpg', fecha_lanzamiento='2022-02-04', stock=95,
                genero=supervivencia, plataforma=pc,
                destacado=False, top_ventas=False, novedad=False, en_descuento=True,
            ),
            dict(
                titulo='Persona 4 Golden',
                descripcion='Persona 4 Golden es la versión mejorada de Persona 4, un JRPG de Atlus. '
                            'El jugador llega a la tranquila ciudad de Inaba y descubre un misterioso canal '
                            'de televisión que atrapa personas en un mundo alternativo.',
                precio='14.99', precio_original=None,
                imagen='p4.avif', fecha_lanzamiento='2020-06-13', stock=220,
                genero=rpg, plataforma=pc,
                destacado=False, top_ventas=True, novedad=False, en_descuento=False,
            ),
            dict(
                titulo='Fear & Hunger',
                descripcion='Fear & Hunger es un RPG de terror de Miro Haverinen. Un oscuro dungeon crawler '
                            'que mezcla elementos de survival horror con combate por turnos. Conocido por su '
                            'dificultad extrema y su atmósfera perturbadora sin concesiones.',
                precio='9.99', precio_original=None,
                imagen='fearHunger.jpg', fecha_lanzamiento='2018-12-08', stock=35,
                genero=terror, plataforma=pc,
                destacado=False, top_ventas=False, novedad=False, en_descuento=False,
            ),
            dict(
                titulo='Lunacid',
                descripcion='Lunacid es un RPG de acción en primera persona inspirado en los clásicos de '
                            'FromSoftware como King\'s Field. El jugador despierta en un pozo profundo y '
                            'debe escapar a través de catacumbas llenas de monstruos y secretos.',
                precio='12.99', precio_original=None,
                imagen='lunacid.jpg', fecha_lanzamiento='2023-07-19', stock=40,
                genero=rpg, plataforma=pc,
                destacado=False, top_ventas=False, novedad=False, en_descuento=False,
            ),
            dict(
                titulo='Metaphor: ReFantazio',
                descripcion='Metaphor: ReFantazio es un JRPG de Atlus Studio Zero, creadores de Persona. '
                            'En un reino de fantasía donde el rey ha muerto, el jugador compite en una '
                            'elección real mientras combate contra monstruos llamados Humans.',
                precio='59.99', precio_original=None,
                imagen='metaphor.avif', fecha_lanzamiento='2024-10-11', stock=100,
                genero=rpg, plataforma=pc,
                destacado=True, top_ventas=False, novedad=True, en_descuento=False,
            ),
            dict(
                titulo='Duck Game',
                descripcion='Duck Game es un juego de acción multijugador frenético donde controlas a un pato '
                            'armado hasta los dientes. Compite con amigos en partidas de un golpe que mezclan '
                            'plataformas con disparos en entornos llenos de trampas y armas absurdas.',
                precio='12.99', precio_original=None,
                imagen='duck.jpg', fecha_lanzamiento='2015-06-05', stock=250,
                genero=accion, plataforma=pc,
                destacado=False, top_ventas=False, novedad=False, en_descuento=False,
            ),
            dict(
                titulo='Monster Hunter: World',
                descripcion='Monster Hunter: World es un juego de acción de Capcom en el que los jugadores '
                            'cazan criaturas colosales en un ecosistema vivo. Con 14 tipos de armas y un sistema '
                            'de crafteo profundo, es uno de los juegos más vendidos de la compañía.',
                precio='24.99', precio_original='39.99',
                imagen='monster.jpg', fecha_lanzamiento='2018-08-09', stock=160,
                genero=accion, plataforma=pc,
                destacado=False, top_ventas=True, novedad=False, en_descuento=True,
            ),
            dict(
                titulo='The Forest',
                descripcion='The Forest es un juego de supervivencia y terror de Endnight Games. '
                            'El jugador sobrevive en un bosque habitado por caníbales mutantes tras estrellarse '
                            'un avión, debiendo construir refugios, conseguir comida y descubrir el misterio de la isla.',
                precio='14.99', precio_original=None,
                imagen='forest.jpg', fecha_lanzamiento='2018-04-30', stock=210,
                genero=supervivencia, plataforma=pc,
                destacado=False, top_ventas=True, novedad=False, en_descuento=False,
            ),
            dict(
                titulo='For Honor',
                descripcion='For Honor es un juego de lucha multijugador de Ubisoft en el que guerreros de '
                            'distintas facciones —caballeros, samuráis y vikingos— se enfrentan en batallas '
                            'épicas usando el sistema de combate Arte de la Batalla.',
                precio='14.99', precio_original='29.99',
                imagen='forHonor.avif', fecha_lanzamiento='2017-02-14', stock=100,
                genero=lucha, plataforma=pc,
                destacado=False, top_ventas=False, novedad=False, en_descuento=True,
            ),
            dict(
                titulo='Final Fantasy VII Remake Intergrade',
                descripcion='Remake completo del clásico de Square Enix. Cloud Strife, un ex-SOLDADO, '
                            'se une al grupo eco-terrorista Avalanche para combatir a la megacorporación Shinra. '
                            'La versión Intergrade incluye el episodio adicional protagonizado por Yuffie.',
                precio='49.99', precio_original=None,
                imagen='ff7.jpg', fecha_lanzamiento='2021-12-16', stock=90,
                genero=rpg, plataforma=pc,
                destacado=True, top_ventas=False, novedad=False, en_descuento=False,
            ),
            dict(
                titulo='Nonexistence',
                descripcion='Nonexistence es un juego de terror psicológico indie que sumerge al jugador '
                            'en una experiencia perturbadora de exploración y supervivencia. '
                            'Con una atmósfera opresiva y narrativa críptica, desafía al jugador a descubrir la verdad.',
                precio='7.99', precio_original=None,
                imagen='nonexistence.jpg', fecha_lanzamiento='2020-10-15', stock=20,
                genero=terror, plataforma=pc,
                destacado=False, top_ventas=False, novedad=False, en_descuento=False,
            ),
            dict(
                titulo='Guilty Gear Xrd REV 2',
                descripcion='Guilty Gear Xrd REV 2 es un juego de lucha de Arc System Works que destaca por '
                            'sus impresionantes gráficos cel-shading que imitan el anime en 3D. '
                            'Ofrece un roster amplio, un modo historia cinematográfico y un sistema de combate profundo.',
                precio='19.99', precio_original='39.99',
                imagen='ggxrd.jpg', fecha_lanzamiento='2017-05-26', stock=65,
                genero=lucha, plataforma=pc,
                destacado=False, top_ventas=False, novedad=False, en_descuento=True,
            ),
            dict(
                titulo='The Binding of Isaac: Repentance',
                descripcion='The Binding of Isaac: Repentance es la expansión definitiva del roguelike de '
                            'Edmund McMillen. Isaac escapa de su madre a través de un sótano lleno de monstruos. '
                            'Con más de 700 objetos, 34 personajes y decenas de finales, es enormemente rejugable.',
                precio='19.99', precio_original=None,
                imagen='isaac.jpg', fecha_lanzamiento='2021-03-31', stock=320,
                genero=roguelike, plataforma=pc,
                destacado=True, top_ventas=True, novedad=False, en_descuento=False,
            ),
            dict(
                titulo='Vambrace: Cold Soul',
                descripcion='Vambrace: Cold Soul es un RPG de exploración roguelike de Devespresso Games. '
                            'El jugador lidera un grupo de aventureros a través de la ciudad helada de Icenaire, '
                            'cursada por los muertos vivientes, en busca de liberar a sus habitantes.',
                precio='14.99', precio_original='24.99',
                imagen='vambrance.jpg', fecha_lanzamiento='2019-05-28', stock=30,
                genero=roguelike, plataforma=switch,
                destacado=False, top_ventas=False, novedad=False, en_descuento=True,
            ),
            dict(
                titulo='Celeste',
                descripcion='Celeste es un juego de plataformas de precisión de Maddy Thorson y Noel Berry. '
                            'Madeline escala la Montaña Celeste enfrentándose no solo a obstáculos físicos, '
                            'sino también a sus propios demonios interiores. Ganador de múltiples premios.',
                precio='19.99', precio_original=None,
                imagen='celeste.avif', fecha_lanzamiento='2018-01-25', stock=230,
                genero=accion, plataforma=pc,
                destacado=False, top_ventas=True, novedad=False, en_descuento=False,
            ),
            dict(
                titulo='Clair Obscur: Expedition 33',
                descripcion='Clair Obscur: Expedition 33 es un RPG por turnos de Sandfall Interactive. '
                            'En un mundo donde la Pintora borra a personas cada año reduciendo su número, '
                            'la Expedición 33 parte a destruirla antes de que llegue su turno.',
                precio='49.99', precio_original=None,
                imagen='expedition.jpg', fecha_lanzamiento='2025-04-24', stock=110,
                genero=rpg, plataforma=pc,
                destacado=True, top_ventas=False, novedad=True, en_descuento=False,
            ),
            dict(
                titulo='Castlevania: Symphony of the Night',
                descripcion='Castlevania: Symphony of the Night es el juego que definió el género metroidvania. '
                            'Alucard, hijo de Drácula, explora el inmenso castillo de su padre en un mundo '
                            'lleno de secretos, con una estructura no lineal revolucionaria para su época.',
                precio='9.99', precio_original=None,
                imagen='castle.jpg', fecha_lanzamiento='1997-03-20', stock=150,
                genero=metroidvania, plataforma=pc,
                destacado=False, top_ventas=False, novedad=False, en_descuento=False,
            ),
            dict(
                titulo='Left 4 Dead 2',
                descripcion='Left 4 Dead 2 es un shooter cooperativo de Valve en el que cuatro supervivientes '
                            'deben escapar de hordas de infectados. Con campañas variadas y el modo Versus, '
                            'sigue siendo uno de los mejores cooperativos de la historia.',
                precio='9.99', precio_original='19.99',
                imagen='l4d2.jpg', fecha_lanzamiento='2009-11-17', stock=450,
                genero=fps, plataforma=pc,
                destacado=False, top_ventas=True, novedad=False, en_descuento=True,
            ),
            dict(
                titulo='Plants vs. Zombies',
                descripcion='Plants vs. Zombies es un juego de estrategia tower defense de PopCap Games. '
                            'El jugador planta plantas con habilidades especiales para detener oleadas de '
                            'zombis que intentan invadir su casa. Clásico accesible y enormemente adictivo.',
                precio='4.99', precio_original=None,
                imagen='pvz.jpg', fecha_lanzamiento='2009-05-05', stock=500,
                genero=accion, plataforma=pc,
                destacado=False, top_ventas=True, novedad=False, en_descuento=False,
            ),
            dict(
                titulo='NieR: Automata',
                descripcion='NieR: Automata es un RPG de acción de PlatinumGames y Square Enix. '
                            'En un futuro devastado, androides de combate luchan contra máquinas alienígenas. '
                            'Destaca por su narrativa filosófica y por requerir múltiples partidas para ver la historia completa.',
                precio='29.99', precio_original='39.99',
                imagen='nier.jpg', fecha_lanzamiento='2017-03-17', stock=175,
                genero=accion, plataforma=pc,
                destacado=True, top_ventas=True, novedad=False, en_descuento=True,
            ),
            dict(
                titulo='Dark Souls III',
                descripcion='Dark Souls III es un RPG de acción de FromSoftware y la entrega final de la '
                            'trilogía Souls. Con un diseño de niveles interconectado, un lore profundo y '
                            'un combate exigente y satisfactorio, es considerado uno de los mejores de la saga.',
                precio='19.99', precio_original='39.99',
                imagen='ds3.jpg', fecha_lanzamiento='2016-04-12', stock=210,
                genero=accion, plataforma=pc,
                destacado=True, top_ventas=True, novedad=False, en_descuento=True,
            ),
            dict(
                titulo='A Plague Tale: Requiem',
                descripcion='A Plague Tale: Requiem es la secuela de Innocence, desarrollada por Asobo Studio. '
                            'Amicia y Hugo huyen hacia el sur de Francia buscando una cura para la maldición '
                            'de Hugo, perseguidos por ratas y la Inquisición en la Europa medieval.',
                precio='39.99', precio_original='49.99',
                imagen='beyond.jpg', fecha_lanzamiento='2022-10-18', stock=80,
                genero=accion, plataforma=pc,
                destacado=False, top_ventas=False, novedad=False, en_descuento=True,
            ),
            dict(
                titulo='Cyberpunk 2077',
                descripcion='Cyberpunk 2077 es un RPG de mundo abierto de CD Projekt Red ambientado en '
                            'Night City, una megalópolis futurista obsesionada con el poder y las modificaciones '
                            'corporales. El jugador encarna a V, un mercenario con un implante de leyenda.',
                precio='29.99', precio_original='59.99',
                imagen='cyberpunk.jfif', fecha_lanzamiento='2020-12-10', stock=200,
                genero=rpg, plataforma=pc,
                destacado=True, top_ventas=False, novedad=False, en_descuento=True,
            ),
            dict(
                titulo='Street Fighter 6',
                descripcion='Street Fighter 6 es el último juego de lucha de Capcom. Introduce el modo '
                            'World Tour con un avatar personalizable, el modo Battle Hub online y un nuevo '
                            'sistema de combate con el Drive System que añade profundidad estratégica.',
                precio='39.99', precio_original=None,
                imagen='sf6.avif', fecha_lanzamiento='2023-06-02', stock=110,
                genero=lucha, plataforma=pc,
                destacado=True, top_ventas=False, novedad=True, en_descuento=False,
            ),
            dict(
                titulo='Tekken 7',
                descripcion='Tekken 7 es el juego de lucha 3D de Bandai Namco que concluye la saga '
                            'de la familia Mishima. Con un extenso roster de luchadores y el modo historia '
                            'cinematográfico, es uno de los juegos de lucha más vendidos de la historia.',
                precio='19.99', precio_original='39.99',
                imagen='tekken7.jpg', fecha_lanzamiento='2017-06-02', stock=155,
                genero=lucha, plataforma=pc,
                destacado=False, top_ventas=True, novedad=False, en_descuento=True,
            ),
            dict(
                titulo='Grand Theft Auto VI',
                descripcion='Grand Theft Auto VI es la nueva entrega de Rockstar Games, ambientada en el '
                            'estado ficticio de Leonida, inspirado en Florida. Por primera vez la saga '
                            'presenta una protagonista femenina junto a Jason en una historia de crimen y ambición.',
                precio='69.99', precio_original=None,
                imagen='gta6.jpg', fecha_lanzamiento='2025-05-26', stock=300,
                genero=accion, plataforma=ps5,
                destacado=True, top_ventas=True, novedad=True, en_descuento=False,
            ),
            dict(
                titulo='Elden Ring',
                descripcion='Elden Ring es un RPG de acción de FromSoftware y George R. R. Martin. '
                            'En las Tierras Intermedias, el jugador busca los fragmentos del Elden Ring '
                            'para convertirse en Señor del Elden. Ganador del GOTY 2022.',
                precio='49.99', precio_original=None,
                imagen='elden.jpg', fecha_lanzamiento='2022-02-25', stock=160,
                genero=accion, plataforma=pc,
                destacado=True, top_ventas=True, novedad=False, en_descuento=False,
            ),
        ]

        for datos in juegos:
            Juego.objects.create(**datos)

        noticias = [
            dict(
                titulo='Clair Obscur: Expedition 33 arrasa en ventas en su primer mes',
                contenido='El debut de Sandfall Interactive ha superado todas las expectativas con más de dos '
                          'millones de copias vendidas en su primer mes. La crítica elogia su fusión de RPG '
                          'por turnos clásico con mecánicas de acción en tiempo real y su narrativa poética.',
                imagen='expedition.jpg',
            ),
            dict(
                titulo='Hollow Knight: Silksong confirma fecha de lanzamiento',
                contenido='Team Cherry ha confirmado oficialmente el lanzamiento de Silksong para junio de 2025. '
                          'La esperada secuela de Hollow Knight llevará a Hornet como protagonista a un nuevo '
                          'reino con más de 150 enemigos y un sistema de combate renovado.',
                imagen='silksong.avif',
            ),
            dict(
                titulo='Grand Theft Auto VI ya disponible: Rockstar rompe récords de ventas',
                contenido='Grand Theft Auto VI ha batido todos los récords de la industria con más de diez '
                          'millones de copias vendidas en su primer fin de semana. El juego, ambientado en '
                          'Leonida, ya es el título con mayores ingresos del primer día en la historia.',
                imagen='gta6.jpg',
            ),
            dict(
                titulo='Street Fighter 6 supera los diez millones de jugadores',
                contenido='Capcom ha anunciado que Street Fighter 6 ha superado los diez millones de jugadores '
                          'registrados. El juego continúa recibiendo nuevos personajes y stages de temporada, '
                          'consolidándose como el mejor juego de lucha de la generación actual.',
                imagen='sf6.avif',
            ),
        ]

        for datos in noticias:
            Noticia.objects.create(**datos)

        self.stdout.write(self.style.SUCCESS(
            f'Base de datos poblada: {len(juegos)} juegos y {len(noticias)} noticias creados.'
        ))
