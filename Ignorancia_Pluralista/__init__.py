from otree.api import *
from collections import defaultdict
import random



class C(BaseConstants):
    NAME_IN_URL = 'Ignorancia_Pluralista'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 5

#NUEVO
class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            self.set_custom_grouping_Prueba()
        elif self.round_number == 2:
            self.set_custom_grouping_Tabaco()
        elif self.round_number == 3:
            self.set_custom_grouping_Arte()
        elif self.round_number == 4:
            self.set_custom_grouping_Violencia()
        elif self.round_number == 5:
            self.set_custom_grouping_Crisis()

    def set_custom_grouping_Prueba(self):
        players = self.get_players()
        group_matrix_Prueba = []
        player_to_group = {p.id_in_subsession: p.participant.vars.get('group_number_Prueba', None) for p in players}

        group_to_players = defaultdict(list)
        for player in players:
            group_id = player_to_group.get(player.id_in_subsession)
            if group_id is not None:
                group_to_players[group_id].append(player)

        # Convertir el diccionario en una matriz de grupos y aleatorizar el orden de los miembros
        for group_id, group_players in group_to_players.items():
            random.shuffle(group_players)  # Aleatorizar el orden dentro de cada grupo
            group_matrix_Prueba.append(group_players)
            for index, player in enumerate(group_players):
                player.participant.vars['order_number_Prueba'] = index + 1  # Asigna el orden aleatorizado

        # Incluir jugadores sin grupo en su propio grupo
        all_players_in_groups = set(p for sublist in group_matrix_Prueba for p in sublist)
        solo_players = [p for p in players if p not in all_players_in_groups]
        for player in solo_players:
            group_matrix_Prueba.append([player])
            player.participant.vars['order_number_Prueba'] = 1  # Asigna el orden a jugadores solos

        print("Matriz de grupos antes de set_group_matrix_Prueba:", group_matrix_Prueba)
        self.set_group_matrix(group_matrix_Prueba)
        print("Matriz de grupos después de set_group_matrix_Prueba:", self.get_group_matrix())
    
    def set_custom_grouping_Tabaco(self):
        players = self.get_players()
        group_matrix_Tabaco = []
        player_to_group = {p.id_in_subsession: p.participant.vars.get('group_number_Tabaco', None) for p in players}

        group_to_players = defaultdict(list)
        for player in players:
            group_id = player_to_group.get(player.id_in_subsession)
            if group_id is not None:
                group_to_players[group_id].append(player)

        # Convertir el diccionario en una matriz de grupos y aleatorizar el orden de los miembros
        for group_id, group_players in group_to_players.items():
            random.shuffle(group_players)  # Aleatorizar el orden dentro de cada grupo
            group_matrix_Tabaco.append(group_players)
            for index, player in enumerate(group_players):
                player.participant.vars['order_number_Tabaco'] = index + 1  # Asigna el orden aleatorizado

        # Incluir jugadores sin grupo en su propio grupo
        all_players_in_groups = set(p for sublist in group_matrix_Tabaco for p in sublist)
        solo_players = [p for p in players if p not in all_players_in_groups]
        for player in solo_players:
            group_matrix_Tabaco.append([player])
            player.participant.vars['order_number_Tabaco'] = 1  # Asigna el orden a jugadores solos

        print("Matriz de grupos antes de set_group_matrix_Tabaco:", group_matrix_Tabaco)
        self.set_group_matrix(group_matrix_Tabaco)
        print("Matriz de grupos después de set_group_matrix_Tabaco:", self.get_group_matrix())

    def set_custom_grouping_Arte(self):
        players = self.get_players()
        group_matrix_Arte = []
        player_to_group = {p.id_in_subsession: p.participant.vars.get('group_number_Arte', None) for p in players}

        group_to_players = defaultdict(list)
        for player in players:
            group_id = player_to_group.get(player.id_in_subsession)
            if group_id is not None:
                group_to_players[group_id].append(player)

        # Convertir el diccionario en una matriz de grupos y aleatorizar el orden de los miembros
        for group_id, group_players in group_to_players.items():
            random.shuffle(group_players)  # Aleatorizar el orden dentro de cada grupo
            group_matrix_Arte.append(group_players)
            for index, player in enumerate(group_players):
                player.participant.vars['order_number_Arte'] = index + 1  # Asigna el orden aleatorizado

        # Incluir jugadores sin grupo en su propio grupo
        all_players_in_groups = set(p for sublist in group_matrix_Arte for p in sublist)
        solo_players = [p for p in players if p not in all_players_in_groups]
        for player in solo_players:
            group_matrix_Arte.append([player])
            player.participant.vars['order_number_Arte'] = 1  # Asigna el orden a jugadores solos

        print("Matriz de grupos antes de set_group_matrix_Arte:", group_matrix_Arte)
        self.set_group_matrix(group_matrix_Arte)
        print("Matriz de grupos después de set_group_matrix_Arte:", self.get_group_matrix())

    def set_custom_grouping_Violencia(self):
        players = self.get_players()
        group_matrix_Violencia = []
        player_to_group = {p.id_in_subsession: p.participant.vars.get('group_number_Violencia', None) for p in players}

        group_to_players = defaultdict(list)
        for player in players:
            group_id = player_to_group.get(player.id_in_subsession)
            if group_id is not None:
                group_to_players[group_id].append(player)

        # Convertir el diccionario en una matriz de grupos y aleatorizar el orden de los miembros
        for group_id, group_players in group_to_players.items():
            random.shuffle(group_players)  # Aleatorizar el orden dentro de cada grupo
            group_matrix_Violencia.append(group_players)
            for index, player in enumerate(group_players):
                player.participant.vars['order_number_Violencia'] = index + 1  # Asigna el orden aleatorizado

        # Incluir jugadores sin grupo en su propio grupo
        all_players_in_groups = set(p for sublist in group_matrix_Violencia for p in sublist)
        solo_players = [p for p in players if p not in all_players_in_groups]
        for player in solo_players:
            group_matrix_Violencia.append([player])
            player.participant.vars['order_number_Violencia'] = 1  # Asigna el orden a jugadores solos

        print("Matriz de grupos antes de set_group_matrix_Violencia:", group_matrix_Violencia)
        self.set_group_matrix(group_matrix_Violencia)
        print("Matriz de grupos después de set_group_matrix_Violencia:", self.get_group_matrix())

    def set_custom_grouping_Crisis(self):
        players = self.get_players()
        group_matrix_Crisis = []
        player_to_group = {p.id_in_subsession: p.participant.vars.get('group_number_Crisis', None) for p in players}

        group_to_players = defaultdict(list)
        for player in players:
            group_id = player_to_group.get(player.id_in_subsession)
            if group_id is not None:
                group_to_players[group_id].append(player)

        # Convertir el diccionario en una matriz de grupos y aleatorizar el orden de los miembros
        for group_id, group_players in group_to_players.items():
            random.shuffle(group_players)  # Aleatorizar el orden dentro de cada grupo
            group_matrix_Crisis.append(group_players)
            for index, player in enumerate(group_players):
                player.participant.vars['order_number_Crisis'] = index + 1  # Asigna el orden aleatorizado

        # Incluir jugadores sin grupo en su propio grupo
        all_players_in_groups = set(p for sublist in group_matrix_Crisis for p in sublist)
        solo_players = [p for p in players if p not in all_players_in_groups]
        for player in solo_players:
            group_matrix_Crisis.append([player])
            player.participant.vars['order_number_Crisis'] = 1  # Asigna el orden a jugadores solos

        print("Matriz de grupos antes de set_group_matrix_Crisis:", group_matrix_Crisis)
        self.set_group_matrix(group_matrix_Crisis)
        print("Matriz de grupos después de set_group_matrix_Crisis:", self.get_group_matrix())


class Group(BaseGroup):
    groups_formed_Prueba = models.BooleanField(initial=False)
    groups_formed_Tabaco = models.BooleanField(initial=False)
    groups_formed_Arte = models.BooleanField(initial=False)
    groups_formed_Violencia = models.BooleanField(initial=False)
    groups_formed_Crisis = models.BooleanField(initial=False)
    current_responder = models.IntegerField(initial=1)
    group_prueba_responses = models.LongStringField()
    group_antitabaco_responses = models.LongStringField()
    group_arte_responses = models.LongStringField()
    group_violencia_responses = models.LongStringField()
    group_crisis_responses = models.LongStringField()
    last_response = models.StringField(initial="")  # Agregar este campo para almacenar la última respuesta


class Player(BasePlayer):
    #Información Personal
    age = models.IntegerField(label='Edad:')
    gender = models.StringField(choices=[['Femenino', 'Femenino'], ['Masculino', 'Masculino'], ['No binarix', 'No binarix']], label='Sexo:')
    programa = models.StringField(choices = [['Licenciatura en Economía', 'Licenciatura en Economía'], ['Licenciatura en Ciencia Política y Relaciones Internacionales', 'Licenciatura en Ciencia Política y Relaciones Internacionales'], ['Licenciatura en Derecho', 'Licenciatura en Derecho'], ['Maestría en Economía', 'Maestría en Economía'], ['Maestría en Ciencia Política', 'Maestría en Ciencia Política']], label='¿En qué programa estás?')
    ingreso = models.StringField(
        label='¿Cuál es tu ingreso mensual aproximado?',
        choices=[
            ['Menos de $4,999', 'Menos de $4,999'],
            ['$4,500-$7,499', '$4,500-$7,499'],
            ['$7,500-$11,499', '$7,500-$11,499'],
            ['$11,500-$14,499', '$11,500-$14,499'],
            ['$15,000-$18,499', '$15,000-$18,499'],
            ['$18,500 o más', '$18,500 o más']
        ]
    )
    participacion = models.StringField(
        label= '¿Has participado en algún experimento de investigación previamente?',
        choices=[
            ['sí', 'sí'],
            ['no', 'no']
        ]
    )

    #Preguntas Controversiales
    antitabaco = models.StringField(
        label= '¿Estás de acuerdo con la nueva ley antitabaco en México?',
        choices=[
            ['De acuerdo', 'De acuerdo'],
            ['En desacuerdo', 'En desacuerdo']
        ]
    )
    arte= models.StringField(
        label= '¿El arte que se exhibe en los museos de arte contemporáneo ya no tiene el mismo virtuosismo que el arte en los museos clásicos?',
        choices=[
            ['Sí tiene el mismo virtuosismo', 'Sí tiene el mismo virtuosismo'],
            ['No tiene el mismo virtuosismo', 'No tiene el mismo virtuosismo']
        ]
    )
    violencia= models.StringField(
        label= '¿Estás de acuerdo con la frase “no hay paz sin la violencia”?',
        choices=[
            ['De acuerdo', 'De acuerdo'],
            ['En desacuerdo', 'En desacuerdo']
        ]
    )
    crisis= models.StringField(
        label= '¿Qué es más importante, afrontar la crisis climática o terminar la pobreza extrema en México?',
        choices=[
            ['Crisis climática', 'Crisis climática'],
            ['La pobreza extrema', 'La pobreza extrema']
        ]
    )

    #Pregunta de prueba
    prueba = models.StringField(
        label= '¿Qué es mejor, las Oreo o las Chokis?',
        choices=[
            ['Oreo', 'Oreo'],
            ['Chokis', 'Chokis']
        ]
    )

    #Pregunta de prueba durante la interacción grupal
    prueba_group = models.StringField(
        label= '¿Qué es mejor, las Oreo o las Chokis?',
        choices=[
            ['Oreo', 'Oreo'],
            ['Chokis', 'Chokis']
        ]
    )

    #Preguntas Controversiales durante la interacción grupal
    antitabaco_group = models.StringField(
        label= '¿Estás de acuerdo con la nueva ley antitabaco en México?',
        choices=[
            ['De acuerdo', 'De acuerdo'],
            ['En desacuerdo', 'En desacuerdo']
        ]
    )

    arte_group= models.StringField(
        label= '¿El arte que se exhibe en los museos de arte contemporáneo ya no tiene el mismo virtuosismo que el arte en los museos clásicos?',
        choices=[
            ['Sí tiene el mismo virtuosismo', 'Sí tiene el mismo virtuosismo'],
            ['No tiene el mismo virtuosismo', 'No tiene el mismo virtuosismo']
        ]
    )

    violencia_group= models.StringField(
        label= '¿Estás de acuerdo con la frase “no hay paz sin la violencia”?',
        choices=[
            ['De acuerdo', 'De acuerdo'],
            ['En desacuerdo', 'En desacuerdo']
        ]
    )

    crisis_group= models.StringField(
        label= '¿Qué es más importante, afrontar la crisis climática o terminar la pobreza extrema en México?',
        choices=[
            ['Crisis climática', 'Crisis climática'],
            ['La pobreza extrema', 'La pobreza extrema']
        ]
    )

    #Preguntas de expectativas para el actor (Prueba)
    Prueba_money_expected1 = models.IntegerField(
        min=0,
        max=10,
        label="¿Cuánto crees que te asignó el miembro 1?"
    )

    Prueba_money_expected2 = models.IntegerField(
        min=0,
        max=10,
        label="¿Cuánto crees que te asignó el miembro 2?"
    )

    Prueba_money_expected3 = models.IntegerField(
        min=0,
        max=10,
        label="¿Cuánto crees que te asignó el miembro 3?"
    )

    Prueba_money_notexpected1 = models.IntegerField(
        min=0,
        max=10,
        label="¿Cuánto crees que te hubiera asignado el miembro 1 si hubieras dicho lo contrario?"
    )

    Prueba_money_notexpected2 = models.IntegerField(
        min=0,
        max=10,
        label="¿Cuánto crees que te hubiera asignado el miembro 2 si hubieras dicho lo contrario?"
    )

    Prueba_money_notexpected3 = models.IntegerField(
        min=0,
        max=10,
        label="¿Cuánto crees que te hubiera asignado el miembro 3 si hubieras dicho lo contrario?"
    )

    Prueba_realtypejueces1 = models.IntegerField(
        min=0,
        max=100,
        label="Del 0 al 100 ¿Qué tan probable es que el miembro 1 prefiera las Oreo?"
    )

    Prueba_realtypejueces2 = models.IntegerField(
        min=0,
        max=100,
        label="Del 0 al 100 ¿Qué tan probable es que el miembro 2 prefiera las Oreo?"
    )

    Prueba_realtypejueces3 = models.IntegerField(
        min=0,
        max=100,
        label="Del 0 al 100 ¿Qué tan probable es que el miembro 3 prefiera las Oreo?"
    )

    #Distribución de dinero y expectativas de los jueces (prueba)
    Prueba_money_to_member1 = models.IntegerField(
        min=0, 
        max=10, 
        label="¿Cuántos de los 10 pesos deseas dar al miembro 1 de tu grupo?"
    )

    Prueba_money_to_member2 = models.IntegerField(
        min=0, 
        max=10, 
        label="¿Cuántos de los 10 pesos deseas dar al miembro 2 de tu grupo?"
    )

    Prueba_money_to_member3 = models.IntegerField(
        min=0,
        max=10,
        label="¿Cuántos de los 10 pesos deseas dar al miembro 3 de tu grupo?"
    )

    Prueba_realtypeactor1 = models.IntegerField(
        min=0,
        max=100,
        label="Del 0 al 100 ¿Qué tan probable es que el miembro 1 prefiera las Oreo?"
    )

    Prueba_realtypeactor2 = models.IntegerField(
        min=0,
        max=100,
        label="Del 0 al 100 ¿Qué tan probable es que el miembro 2 prefiera las Oreo?"
    )

    Prueba_realtypeactor3 = models.IntegerField(
        min=0,
        max=100,
        label="Del 0 al 100 ¿Qué tan probable es que el miembro 3 prefiera las Oreo?"
    )

    Prueba_realtypejuez1 = models.IntegerField(
        min=0,
        max=100,
        label="Del 0 al 100 ¿Qué tan probable es que el miembro 1 (que juega el papel de juez junto contigo) prefiera las Oreo? Si tu eres el miembro 1 responde con base en tu opinión verdadera"
    )

    Prueba_realtypejuez2 = models.IntegerField(
        min=0,
        max=100,
        label="Del 0 al 100 ¿Qué tan probable es que el miembro 2 (que juega el papel de juez junto contigo) prefiera las Oreo? Si tu eres el miembro 2 responde con base en tu opinión verdadera"
    )

    Prueba_realtypejuez3 = models.IntegerField(
        min=0,
        max=100,
        label="Del 0 al 100 ¿Qué tan probable es que el miembro 3 (que juega el papel de juez junto contigo) prefiera las Oreo? Si tu eres el miembro 3 responde con base en tu opinión verdadera"
    )

    #Preguntas de expectativas para el actor (Tabaco)
    Tabaco_money_expected1 = models.IntegerField(
        min=0,
        max=10,
        label="¿Cuánto crees que te asignó el miembro 1?"
    )

    Tabaco_money_expected2 = models.IntegerField(
        min=0,
        max=10,
        label="¿Cuánto crees que te asignó el miembro 2?"
    )

    Tabaco_money_expected3 = models.IntegerField(
        min=0,
        max=10,
        label="¿Cuánto crees que te asignó el miembro 3?"
    )

    Tabaco_money_notexpected1 = models.IntegerField(
        min=0,
        max=10,
        label="¿Cuánto crees que te hubiera asignado el miembro 1 si hubieras dicho lo contrario?"
    )

    Tabaco_money_notexpected2 = models.IntegerField(
        min=0,
        max=10,
        label="¿Cuánto crees que te hubiera asignado el miembro 2 si hubieras dicho lo contrario?"
    )

    Tabaco_money_notexpected3 = models.IntegerField(
        min=0,
        max=10,
        label="¿Cuánto crees que te hubiera asignado el miembro 3 si hubieras dicho lo contrario?"
    )

    Tabaco_realtypejueces1 = models.IntegerField(
        min=0,
        max=100,
        label="Del 0 al 100 ¿Qué tan probable es que el miembro 1 esté de acuerdo con la ley?"
    )

    Tabaco_realtypejueces2 = models.IntegerField(
        min=0,
        max=100,
        label="Del 0 al 100 ¿Qué tan probable es que el miembro 2 esté de acuerdo con la ley?"
    )

    Tabaco_realtypejueces3 = models.IntegerField(
        min=0,
        max=100,
        label="Del 0 al 100 ¿Qué tan probable es que el miembro 3 esté de acuerdo con la ley?"
    )

    #Distribución de dinero y expectativas de los jueces (tabaco)
    Tabaco_money_to_member1 = models.IntegerField(
        min=0, 
        max=10, 
        label="¿Cuántos de los 10 pesos deseas dar al miembro 1 de tu grupo?"
    )

    Tabaco_money_to_member2 = models.IntegerField(
        min=0, 
        max=10, 
        label="¿Cuántos de los 10 pesos deseas dar al miembro 2 de tu grupo?"
    )

    Tabaco_money_to_member3 = models.IntegerField(
        min=0, 
        max=10, 
        label="¿Cuántos de los 10 pesos deseas dar al miembro 3 de tu grupo?"
    )

    Tabaco_realtypeactor1 = models.IntegerField(
        min=0,
        max=100,
        label="Del 0 al 100 ¿Qué tan probable es que el miembro 1 esté de acuerdo con la ley?"
    )

    Tabaco_realtypeactor2 = models.IntegerField(
        min=0,
        max=100,
        label="Del 0 al 100 ¿Qué tan probable es que el miembro 2 esté de acuerdo con la ley?"
    )

    Tabaco_realtypeactor3 = models.IntegerField(
        min=0,
        max=100,
        label="Del 0 al 100 ¿Qué tan probable es que el miembro 3 esté de acuerdo con la ley?"
    )

    Tabaco_realtypejuez1 = models.IntegerField(
        min=0,
        max=100,
        label="Del 0 al 100 ¿Qué tan probable es que el miembro 1 (que juega el papel de juez junto contigo) esté de acuerdo con la ley? Si tu eres el miembro 1 responde con base en tu opinión verdadera"
    )

    Tabaco_realtypejuez2 = models.IntegerField(
        min=0,
        max=100,
        label="Del 0 al 100 ¿Qué tan probable es que el miembro 2 (que juega el papel de juez junto contigo) esté de acuerdo con la ley? Si tu eres el miembro 2 responde con base en tu opinión verdadera"
    )

    Tabaco_realtypejuez3 = models.IntegerField(
        min=0,
        max=100,
        label="Del 0 al 100 ¿Qué tan probable es que el miembro 3 (que juega el papel de juez junto contigo) esté de acuerdo con la ley? Si tu eres el miembro 3 responde con base en tu opinión verdadera"
    )

    #Preguntas de expectativas para el actor (Arte)
    Arte_money_expected1 = models.IntegerField(
        min=0,
        max=10,
        label="¿Cuánto crees que te asignó el miembro 1?"
    )

    Arte_money_expected2 = models.IntegerField(
        min=0,
        max=10,
        label="¿Cuánto crees que te asignó el miembro 2?"
    )

    Arte_money_expected3 = models.IntegerField(
        min=0,
        max=10,
        label="¿Cuánto crees que te asignó el miembro 3?"
    )

    Arte_money_notexpected1 = models.IntegerField(
        min=0,
        max=10,
        label="¿Cuánto crees que te hubiera asignado el miembro 1 si hubieras dicho lo contrario?"
    )

    Arte_money_notexpected2 = models.IntegerField(
        min=0,
        max=10,
        label="¿Cuánto crees que te hubiera asignado el miembro 2 si hubieras dicho lo contrario?"
    )

    Arte_money_notexpected3 = models.IntegerField(
        min=0,
        max=10,
        label="¿Cuánto crees que te hubiera asignado el miembro 3 si hubieras dicho lo contrario?"
    )

    Arte_realtypejueces1 = models.IntegerField(
        min=0,
        max=100,
        label="Del 0 al 100 ¿Qué tan probable es que el miembro 1 crea que el arte contemporáneo si tiene el mismo virtuosismo?"
    )

    Arte_realtypejueces2 = models.IntegerField(
        min=0,
        max=100,
        label="Del 0 al 100 ¿Qué tan probable es que el miembro 2 crea que el arte contemporáneo si tiene el mismo virtuosismo?"
    )

    Arte_realtypejueces3 = models.IntegerField(
        min=0,
        max=100,
        label="Del 0 al 100 ¿Qué tan probable es que el miembro 3 crea que el arte contemporáneo si tiene el mismo virtuosismo?"
    )

    #Distribución de dinero y expectativas de los jueces (arte)
    Arte_money_to_member1 = models.IntegerField(
        min=0, 
        max=10, 
        label="¿Cuántos de los 10 pesos deseas dar al miembro 1 de tu grupo?"
    )

    Arte_money_to_member2 = models.IntegerField(
        min=0, 
        max=10, 
        label="¿Cuántos de los 10 pesos deseas dar al miembro 2 de tu grupo?"
    )

    Arte_money_to_member3 = models.IntegerField(
        min=0, 
        max=10, 
        label="¿Cuántos de los 10 pesos deseas dar al miembro 3 de tu grupo?"
    )

    Arte_realtypeactor1 = models.IntegerField(
        min=0,
        max=100,
        label="Del 0 al 100 ¿Qué tan probable es que el miembro 1 crea que el arte contemporáneo si tiene el mismo virtuosismo?"
    )

    Arte_realtypeactor2 = models.IntegerField(
        min=0,
        max=100,
        label="Del 0 al 100 ¿Qué tan probable es que el miembro 2 crea que el arte contemporáneo si tiene el mismo virtuosismo?"
    )

    Arte_realtypeactor3 = models.IntegerField(
        min=0,
        max=100,
        label="Del 0 al 100 ¿Qué tan probable es que el miembro 3 crea que el arte contemporáneo si tiene el mismo virtuosismo?"
    )

    Arte_realtypejuez1 = models.IntegerField(
        min=0,
        max=100,
        label="Del 0 al 100 ¿Qué tan probable es que el miembro 1 (que juega el papel de juez junto contigo) crea que el arte contemporáneo si tiene el mismo virtuosismo? Si tu eres el miembro 1 responde con base en tu opinión verdadera"
    )

    Arte_realtypejuez2 = models.IntegerField(
        min=0,
        max=100,
        label="Del 0 al 100 ¿Qué tan probable es que el miembro 2 (que juega el papel de juez junto contigo) crea que el arte contemporáneo si tiene el mismo virtuosismo? Si tu eres el miembro 2 responde con base en tu opinión verdadera"
    )

    Arte_realtypejuez3 = models.IntegerField(
        min=0,
        max=100,
        label="Del 0 al 100 ¿Qué tan probable es que el miembro 3 (que juega el papel de juez junto contigo) crea que el arte contemporáneo si tiene el mismo virtuosismo? Si tu eres el miembro 3 responde con base en tu opinión verdadera"
    )

    #Preguntas de expectativas para el actor (Violencia)
    Violencia_money_expected1 = models.IntegerField(
        min=0,
        max=10,
        label="¿Cuánto crees que te asignó el miembro 1?"
    )

    Violencia_money_expected2 = models.IntegerField(
        min=0,
        max=10,
        label="¿Cuánto crees que te asignó el miembro 2?"
    )

    Violencia_money_expected3 = models.IntegerField(
        min=0,
        max=10,
        label="¿Cuánto crees que te asignó el miembro 3?"
    )

    Violencia_money_notexpected1 = models.IntegerField(
        min=0,
        max=10,
        label="¿Cuánto crees que te hubiera asignado el miembro 1 si hubieras dicho lo contrario?"
    )

    Violencia_money_notexpected2 = models.IntegerField(
        min=0,
        max=10,
        label="¿Cuánto crees que te hubiera asignado el miembro 2 si hubieras dicho lo contrario?"
    )

    Violencia_money_notexpected3 = models.IntegerField(
        min=0,
        max=10,
        label="¿Cuánto crees que te hubiera asignado el miembro 3 si hubieras dicho lo contrario?"
    )

    Violencia_realtypejueces1 = models.IntegerField(
        min=0,
        max=100,
        label="Del 0 al 100 ¿Qué tan probable es que el miembro 1 esté de acuerdo con la frase?"
    )

    Violencia_realtypejueces2 = models.IntegerField(
        min=0,
        max=100,
        label="Del 0 al 100 ¿Qué tan probable es que el miembro 2 esté de acuerdo con la frase?"
    )

    Violencia_realtypejueces3 = models.IntegerField(
        min=0,
        max=100,
        label="Del 0 al 100 ¿Qué tan probable es que el miembro 3 esté de acuerdo con la frase?"
    )

    #Distribución de dinero y expectativas de los jueces (violencia)
    Violencia_money_to_member1 = models.IntegerField(
        min=0, 
        max=10, 
        label="¿Cuántos de los 10 pesos deseas dar al miembro 1 de tu grupo?"
    )

    Violencia_money_to_member2 = models.IntegerField(
        min=0, 
        max=10, 
        label="¿Cuántos de los 10 pesos deseas dar al miembro 2 de tu grupo?"
    )

    Violencia_money_to_member3 = models.IntegerField(
        min=0, 
        max=10, 
        label="¿Cuántos de los 10 pesos deseas dar al miembro 3 de tu grupo?"
    )

    Violencia_realtypeactor1 = models.IntegerField(
        min=0,
        max=100,
        label="Del 0 al 100 ¿Qué tan probable es que el miembro 1 esté de acuerdo con la frase?"
    )

    Violencia_realtypeactor2 = models.IntegerField(
        min=0,
        max=100,
        label="Del 0 al 100 ¿Qué tan probable es que el miembro 2 esté de acuerdo con la frase?"
    )

    Violencia_realtypeactor3 = models.IntegerField(
        min=0,
        max=100,
        label="Del 0 al 100 ¿Qué tan probable es que el miembro 3 esté de acuerdo con la frase?"
    )

    Violencia_realtypejuez1 = models.IntegerField(
        min=0,
        max=100,
        label="Del 0 al 100 ¿Qué tan probable es que el miembro 1 (que juega el papel de juez junto contigo) esté de acuerdo con la frase? Si tu eres el miembro 1 responde con base en tu opinión verdadera"
    )

    Violencia_realtypejuez2 = models.IntegerField(
        min=0,
        max=100,
        label="Del 0 al 100 ¿Qué tan probable es que el miembro 2 (que juega el papel de juez junto contigo) esté de acuerdo con la frase? Si tu eres el miembro 2 responde con base en tu opinión verdadera"
    )

    Violencia_realtypejuez3 = models.IntegerField(
        min=0,
        max=100,
        label="Del 0 al 100 ¿Qué tan probable es que el miembro 3 (que juega el papel de juez junto contigo) esté de acuerdo con la frase? Si tu eres el miembro 3 responde con base en tu opinión verdadera"
    )

    #Preguntas de expectativas para el actor (Crisis)
    Crisis_money_expected1 = models.IntegerField(
        min=0,
        max=10,
        label="¿Cuánto crees que te asignó el miembro 1?"
    )

    Crisis_money_expected2 = models.IntegerField(
        min=0,
        max=10,
        label="¿Cuánto crees que te asignó el miembro 2?"
    )

    Crisis_money_expected3 = models.IntegerField(
        min=0,
        max=10,
        label="¿Cuánto crees que te asignó el miembro 3?"
    )

    Crisis_money_notexpected1 = models.IntegerField(
        min=0,
        max=10,
        label="¿Cuánto crees que te hubiera asignado el miembro 1 si hubieras dicho lo contrario?"
    )

    Crisis_money_notexpected2 = models.IntegerField(
        min=0,
        max=10,
        label="¿Cuánto crees que te hubiera asignado el miembro 2 si hubieras dicho lo contrario?"
    )

    Crisis_money_notexpected3 = models.IntegerField(
        min=0,
        max=10,
        label="¿Cuánto crees que te hubiera asignado el miembro 3 si hubieras dicho lo contrario?"
    )

    Crisis_realtypejueces1 = models.IntegerField(
        min=0,
        max=100,
        label="Del 0 al 100 ¿Qué tan probable es que el miembro 1 crea que es más importante la crisis climática?"
    )

    Crisis_realtypejueces2 = models.IntegerField(
        min=0,
        max=100,
        label="Del 0 al 100 ¿Qué tan probable es que el miembro 2 crea que es más importante la crisis climática?"
    )

    Crisis_realtypejueces3 = models.IntegerField(
        min=0,
        max=100,
        label="Del 0 al 100 ¿Qué tan probable es que el miembro 3 crea que es más importante la crisis climática?"
    )

    #Distribución de dinero y expectativas de los jueces (crisis)
    Crisis_money_to_member1 = models.IntegerField(
        min=0, 
        max=10, 
        label="¿Cuántos de los 10 pesos deseas dar al miembro 1 de tu grupo?"
    )

    Crisis_money_to_member2 = models.IntegerField(
        min=0, 
        max=10, 
        label="¿Cuántos de los 10 pesos deseas dar al miembro 2 de tu grupo?"
    )

    Crisis_money_to_member3 = models.IntegerField(
        min=0, 
        max=10, 
        label="¿Cuántos de los 10 pesos deseas dar al miembro 3 de tu grupo?"
    )

    Crisis_realtypeactor1 = models.IntegerField(
        min=0,
        max=100,
        label="Del 0 al 100 ¿Qué tan probable es que el miembro 1 crea que es más importante la crisis climática?"
    )

    Crisis_realtypeactor2 = models.IntegerField(
        min=0,
        max=100,
        label="Del 0 al 100 ¿Qué tan probable es que el miembro 2 crea que es más importante la crisis climática?"
    )

    Crisis_realtypeactor3 = models.IntegerField(
        min=0,
        max=100,
        label="Del 0 al 100 ¿Qué tan probable es que el miembro 3 crea que es más importante la crisis climática?"
    )

    Crisis_realtypejuez1 = models.IntegerField(
        min=0,
        max=100,
        label="Del 0 al 100 ¿Qué tan probable es que el miembro 1 (que juega el papel de juez junto contigo) crea que es más importante la crisis climática? Si tu eres el miembro 1 responde con base en tu opinión verdadera"
    )

    Crisis_realtypejuez2 = models.IntegerField(
        min=0,
        max=100,
        label="Del 0 al 100 ¿Qué tan probable es que el miembro 2 (que juega el papel de juez junto contigo) crea que es más importante la crisis climática? Si tu eres el miembro 2 responde con base en tu opinión verdadera"
    )

    Crisis_realtypejuez3 = models.IntegerField(
        min=0,
        max=100,
        label="Del 0 al 100 ¿Qué tan probable es que el miembro 3 (que juega el papel de juez junto contigo) crea que es más importante la crisis climática? Si tu eres el miembro 3 responde con base en tu opinión verdadera"
    )

#Orden del experimento

class Introduction(Page):
    form_model = 'player'
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return dict(next_button_label="Continuar a Primer Periodo")

class Personal_Information(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'programa', 'ingreso', 'participacion']
    def is_displayed(self):
        return self.round_number == 1
    
    def vars_for_template(self):
        return dict(next_button_label="Continuar a Preguntas")

class Controversial_Questions(Page):
    form_model = 'player'
    form_fields = ['antitabaco', 'arte', 'violencia', 'crisis']
    def is_displayed(self):
        return self.round_number == 1
    
    def vars_for_template(self):
        return dict(next_button_label="Continuar")
    
    def before_next_page(self, timeout_happened):
        # Guardar el valor de 'tabaco', 'arte', 'violencia' y 'crisis' en participant.vars para usarlo en rondas futuras
        self.participant.vars['antitabaco'] = self.antitabaco
        self.participant.vars['arte'] = self.arte
        self.participant.vars['violencia'] = self.violencia
        self.participant.vars['crisis'] = self.crisis

class Prueba_Question(Page):
    form_model = 'player'
    form_fields = ['prueba']
    def is_displayed(self):
        return self.round_number == 1
    
    def vars_for_template(self):
        return dict(next_button_label="Continuar")

#Formación de grupos (prueba)
    
class Forming_Groups_WaitPage_Prueba(WaitPage):
    def is_displayed(self):
        return self.round_number == 1

    def body_text(self):
        return "Gracias por responder a las preguntas. Por favor espere a la indicación del encargado.<br><br>Favor de esperar a que todos los participantes hayan respondido a las preguntas."

    @staticmethod
    def after_all_players_arrive(group: Group):
        print("Inicio de la formación de grupos...")
        if not group.session.vars.get('groups_formed_Prueba', False):
            players = group.get_players()
            option_counts = {'Oreo': 0, 'Chokis': 0}
            remaining_players = players.copy()
    
            for p in players:
                option_counts[p.prueba] += 1

            group_number_Prueba = 1
            order_number_Prueba = 1

            while option_counts['Oreo'] >= 7 and option_counts['Chokis'] >= 7:
                print(f"Intentando formar un grupo bajo las condiciones actuales... Grupo Número: {group_number_Prueba}")
                contexto_seleccionado = random.choice(['Alto', 'Bajo'])
                print(f"Contexto seleccionado: {contexto_seleccionado}")

                agreed_players = [p for p in remaining_players if p.prueba == 'Oreo']
                disagreed_players = [p for p in remaining_players if p.prueba == 'Chokis']

                if contexto_seleccionado == 'Alto':
                    # Proceso específico para Contexto Alto
                    temp_population = random.sample(agreed_players, 7) + random.sample(disagreed_players, 3)
                    selected_players = random.sample(temp_population, 3)
                elif contexto_seleccionado == 'Bajo':
                    # Proceso específico para Contexto Bajo
                    if random.choice(['7-3', '3-7']) == '7-3':
                        temp_population = random.sample(agreed_players, 7) + random.sample(disagreed_players, 3)
                    else:
                        temp_population = random.sample(agreed_players, 3) + random.sample(disagreed_players, 7)
                    selected_players = random.sample(temp_population, 3)
                
                # Asignar contexto y actualizar contadores
                for player in selected_players:
                    player.participant.vars['context_Prueba'] = f"Contexto {contexto_seleccionado}"
                    player.participant.vars['group_number_Prueba'] = group_number_Prueba
                    player.participant.vars['order_number_Prueba'] = order_number_Prueba  # Asignar número de orden
                    order_number_Prueba += 1
                    remaining_players.remove(player)
                    option_counts[player.prueba] -= 1

                group_number_Prueba += 1
                order_number_Prueba = 1  # Reiniciar el número de orden para el próximo grupo


                # Recalcular la disponibilidad de jugadores
                option_counts['Oreo'] = len([p for p in remaining_players if p.prueba == 'Oreo'])
                option_counts['Chokis'] = len([p for p in remaining_players if p.prueba == 'Chokis'])

            # Inicio de la formación de grupos 'Sin Contexto'
            print("Formando grupos 'Sin Contexto' con los jugadores restantes...")
            while len(remaining_players) >= 3:
                # Selecciona aleatoriamente 3 jugadores de los que quedan
                selected_players = random.sample(remaining_players, 3)
                for player in selected_players:
                    player.participant.vars['context_Prueba'] = "Sin Contexto"
                    player.participant.vars['group_number_Prueba'] = group_number_Prueba
                    # Es importante remover a los jugadores seleccionados de la lista de remaining_players
                    remaining_players = [p for p in remaining_players if p not in selected_players]
                print(f"Grupo {group_number_Prueba} formado con 'Sin Contexto'.")
                group_number_Prueba += 1

            # Si después de formar grupos de 3 quedan 1 o 2 jugadores, se les asigna al último grupo 'Sin Contexto'
            if remaining_players:
                for player in remaining_players:
                    player.participant.vars['context_Prueba'] = "Sin Contexto"
                    player.participant.vars['group_number_Prueba'] = group_number_Prueba
                print(f"Jugadores restantes asignados al grupo {group_number_Prueba} con 'Sin Contexto'.")
                # No incrementamos group_number aquí porque estamos agregando a los jugadores restantes al último grupo formado.

            group.session.vars['groups_formed_Prueba'] = True
            print("Todos los grupos han sido formados correctamente.")
        
        group.groups_formed_Prueba = True


class GroupingSyncWaitPage_Prueba(WaitPage):
    def is_displayed(self):
        return self.round_number == 1

    def after_all_players_arrive(self):
        # Llama al método set_custom_grouping directamente, no como una cadena
        self.subsession.set_custom_grouping_Prueba()
   

class ShowContext_Prueba(Page):
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        context_Prueba = self.participant.vars.get('context_Prueba', 'Sin Contexto')
        order_number_Prueba = self.participant.vars.get('order_number_Prueba', 1)

        if context_Prueba == "Contexto Alto":
            message_Prueba = f"""Bienvenido a la ronda de prueba del experimento. Gracias por la espera, reunimos la información de todas las respuestas de los participantes. Para esta sección te hemos colocado en un grupo con otras dos personas. Van a tomar turnos para responder la siguiente pregunta en frente de los demás: ¿Qué es mejor, las Oreo o las Chokis?. A cada uno le asignamos un número que representa el orden en el que responderán a la pregunta, el tuyo es el {order_number_Prueba}.

Creamos el grupo a partir de una población de 10 personas. De estas 10, 7 eligieron “Oreo” y 3 eligieron “Chokis" a la pregunta: ¿Qué es mejor, las Oreo o las Chokis?. Escogimos a cada uno de los integrantes aleatoriamente."""
        elif context_Prueba == "Contexto Bajo":
            message_Prueba = f"""Bienvenido a la ronda de prueba del experimento. Gracias por la espera, reunimos la información de todas las respuestas de los participantes. Para esta sección te hemos colocado en un grupo con otras dos personas. Van a tomar turnos para responder la siguiente pregunta en frente de los demás: ¿Qué es mejor, las Oreo o las Chokis?. A cada uno le asignamos un número que representa el orden en el que responderán a la pregunta, el tuyo es el {order_number_Prueba}.

Creamos el grupo tras seleccionar aleatoriamente a una de las dos poblaciones disponibles, cada una con 10 personas, para el presente experimento. La primera población, con una probabilidad del 50%, donde 7 de las personas eligieron “Oreo” y 3 eligieron “Chokis” a la pregunta: ¿Qué es mejor, las Oreo o las Chokis?. La segunda población, con una probabilidad del 50%, donde 3 de las personas eligieron “Oreo” y 7 eligieron “Chokis” a la pregunta: ¿Qué es mejor, las Oreo o las Chokis?. Escogimos a cada uno de los integrantes aleatoriamente."""
        elif context_Prueba == "Sin Contexto":
            message_Prueba = f"""Bienvenido a la ronda de prueba del experimento. Gracias por la espera, reunimos la información de todas las respuestas de los participantes. Para esta sección te hemos colocado en un grupo con otras dos personas. Van a tomar turnos para responder la siguiente pregunta en frente de los demás: ¿Qué es mejor, las Oreo o las Chokis?. A cada uno le asignamos un número que representa el orden en el que responderán a la pregunta, el tuyo es el {order_number_Prueba}. Creamos el grupo aleatoriamente."""

        return {
            'context_text_Prueba': context_Prueba,
            'message_Prueba': message_Prueba,
            'next_button_label': "Continuar"
        }


# Interacción Grupal Prueba
class PruebaQuestion1(Page):
    form_model = 'player'
    form_fields = ['prueba_group']

    def is_displayed(self):
        return self.round_number == 1 and self.participant.vars['order_number_Prueba'] == 1
    
    def vars_for_template(self):
        return dict(next_button_label="Continuar")

    def before_next_page(self, timeout_happened):
        self.group.current_responder = 2

class PruebaWaitForMember1(WaitPage):
    def is_displayed(self):
        return self.round_number == 1
    
    def after_all_players_arrive(self):
        if self.group.current_responder == 2:
            return  # Permite que el miembro 2 avance a su pregunta
        
class PruebaShowResponseMember1(Page):
    def is_displayed(self):
        return self.round_number == 1
    
    def vars_for_template(self):
        member1 = self.group.get_player_by_id(1)
        return {'member1_response': member1.prueba_group,
                'next_button_label': "Continuar"}
    
class PruebaQuestionsForMember1(Page):
    form_model = 'player'
    form_fields = ['Prueba_money_expected2', 'Prueba_money_expected3', 'Prueba_money_notexpected2', 'Prueba_money_notexpected3', 'Prueba_realtypejueces2', 'Prueba_realtypejueces3']
    
    def is_displayed(self):
        return self.round_number == 1 and self.participant.vars['order_number_Prueba'] == 1
    
    def vars_for_template(self):
        return dict(next_button_label="Continuar")

class PruebaDistributeMoneyPage1(Page):
    form_model = 'player'
    form_fields = ['Prueba_money_to_member1', 'Prueba_realtypeactor1', 'Prueba_realtypejuez2', 'Prueba_realtypejuez3' ]

    def is_displayed(self):
        # Solo se muestra para los miembros 2 y 3
        return self.round_number == 1 and self.participant.vars['order_number_Prueba'] in [2, 3]
    
    def vars_for_template(self):
        member1 = self.group.get_player_by_id(1)
        return {'member1_response': member1.prueba_group,
                'next_button_label': "Continuar"}
    
    
class PruebaWaitForMoneyDistribution1(WaitPage):
    def is_displayed(self):
        return self.round_number == 1
    
    def after_all_players_arrive(self):
        return  # Esto asegura que todos hayan pasado por DistributeMoneyPage antes de continuar


class PruebaQuestion2(Page):
    form_model = 'player'
    form_fields = ['prueba_group']
    def is_displayed(self):
        return self.round_number == 1 and self.participant.vars['order_number_Prueba'] == 2
    def before_next_page(self, timeout_happened):
        self.group.current_responder = 3  # Indica que ahora es el turno del miembro 3
    def vars_for_template(self):
        return dict(next_button_label="Continuar")


class PruebaWaitForMember2(WaitPage):
    def is_displayed(self):
        return self.round_number == 1
    
    def after_all_players_arrive(self):
        if self.group.current_responder == 3:
            return  # Permite que el miembro 3 avance a su pregunta
        
class PruebaShowResponseMember2(Page):
    def is_displayed(self):
        return self.round_number == 1
    
    def vars_for_template(self):
        member2 = self.group.get_player_by_id(2)
        return {'member2_response': member2.prueba_group,
                'next_button_label': "Continuar"}
    
class PruebaQuestionsForMember2(Page):
    form_model = 'player'
    form_fields = ['Prueba_money_expected1', 'Prueba_money_expected3', 'Prueba_money_notexpected1', 'Prueba_money_notexpected3', 'Prueba_realtypejueces1', 'Prueba_realtypejueces3']
    
    def is_displayed(self):
        return self.round_number == 1 and self.participant.vars['order_number_Prueba'] == 2
        
    def vars_for_template(self):
        return dict(next_button_label="Continuar")

class PruebaDistributeMoneyPage2(Page):
    form_model = 'player'
    form_fields = ['Prueba_money_to_member2', 'Prueba_realtypeactor2', 'Prueba_realtypejuez1', 'Prueba_realtypejuez3' ]

    def is_displayed(self):
        # Solo se muestra para los miembros 1 y 3
        return self.round_number == 1 and self.participant.vars['order_number_Prueba'] in [1, 3]
    
    def vars_for_template(self):
        member2 = self.group.get_player_by_id(2)
        return {'member2_response': member2.prueba_group,
                'next_button_label': "Continuar"}
    
class PruebaWaitForMoneyDistribution2(WaitPage):
    def is_displayed(self):
        return self.round_number == 1
    
    def after_all_players_arrive(self):
        return  # Esto asegura que todos hayan pasado por DistributeMoneyPage antes de continuar

class PruebaQuestion3(Page):
    form_model = 'player'
    form_fields = ['prueba_group']
    def is_displayed(self):
        return self.round_number == 1 and self.participant.vars['order_number_Prueba'] == 3
    def before_next_page(self, timeout_happened):
        self.group.current_responder = 4  # Indica que todos han completado
    def vars_for_template(self):
        return dict(next_button_label="Continuar")

class PruebaWaitForMember3(WaitPage):
    def is_displayed(self):
        return self.round_number == 1
    
    def after_all_players_arrive(self):
        if self.group.current_responder == 4:
            return  # Permite que el miembro 3 avance a su pregunta
        
class PruebaShowResponseMember3(Page):
    def is_displayed(self):
        return self.round_number == 1
    
    def vars_for_template(self):
        member3 = self.group.get_player_by_id(3)
        return {'member3_response': member3.prueba_group,
                'next_button_label': "Continuar"}
    
class PruebaQuestionsForMember3(Page):
    form_model = 'player'
    form_fields = ['Prueba_money_expected1', 'Prueba_money_expected2', 'Prueba_money_notexpected1', 'Prueba_money_notexpected2', 'Prueba_realtypejueces1', 'Prueba_realtypejueces2']
    
    def is_displayed(self):
        return self.round_number == 1 and self.participant.vars['order_number_Prueba'] == 3
        
    def vars_for_template(self):
        return dict(next_button_label="Continuar")

class PruebaDistributeMoneyPage3(Page):
    form_model = 'player'
    form_fields = ['Prueba_money_to_member3', 'Prueba_realtypeactor3', 'Prueba_realtypejuez1', 'Prueba_realtypejuez2' ]

    def is_displayed(self):
        # Solo se muestra para los miembros 1 y 3
        return self.round_number == 1 and self.participant.vars['order_number_Prueba'] in [1, 2]
    
    def vars_for_template(self):
        member3 = self.group.get_player_by_id(3)
        return {'member3_response': member3.prueba_group,
                'next_button_label': "Continuar"}
    
class PruebaWaitForMoneyDistribution3(WaitPage):
    def is_displayed(self):
        return self.round_number == 1
    
    def after_all_players_arrive(self):
        return  # Esto asegura que todos hayan pasado por DistributeMoneyPage antes de continuar

#Formación de grupos (tabaco)
    
class GlobalSyncWaitPage_Tabaco(WaitPage):
    wait_for_all_groups = True

    def is_displayed(self):
        return self.round_number == 2

    def after_all_players_arrive(self):
        self.session.vars['groups_formed_Tabaco'] = False
        print("Variables reseteadas, listo para formar grupos para Tabaco.")

class Forming_Groups_WaitPage_Tabaco(WaitPage):
    def is_displayed(self):
        return self.round_number == 2

    def body_text(self):
        return "Gracias por responder a las preguntas. Por favor espere a la indicación del encargado.<br><br>Favor de esperar a que todos los participantes hayan respondido a las preguntas."

    @staticmethod
    def after_all_players_arrive(group: Group):
        print("Inicio de la formación de grupos...")
        if not group.session.vars.get('groups_formed_Tabaco', False):
            players = group.get_players()
            option_counts = {'De acuerdo': 0, 'En desacuerdo': 0}
            remaining_players = players.copy()
    
            for p in players:
                # Aquí obtienes el valor de 'arte' desde las variables de participante, asumiendo que fue guardado allí previamente
                tabaco_value = p.participant.vars.get('antitabaco', '')
                if tabaco_value:
                    option_counts[tabaco_value] += 1
                    p.antitabaco = tabaco_value

            group_number_Tabaco = 1
            order_number_Tabaco = 1

            while option_counts['De acuerdo'] >= 7 and option_counts['En desacuerdo'] >= 7:
                print(f"Intentando formar un grupo bajo las condiciones actuales... Grupo Número: {group_number_Tabaco}")
                contexto_seleccionado = random.choice(['Alto', 'Bajo'])
                print(f"Contexto seleccionado: {contexto_seleccionado}")

                agreed_players = [p for p in remaining_players if p.antitabaco == 'De acuerdo']
                disagreed_players = [p for p in remaining_players if p.antitabaco == 'En desacuerdo']

                if contexto_seleccionado == 'Alto':
                    # Proceso específico para Contexto Alto
                    temp_population = random.sample(agreed_players, 7) + random.sample(disagreed_players, 3)
                    selected_players = random.sample(temp_population, 3)
                elif contexto_seleccionado == 'Bajo':
                    # Proceso específico para Contexto Bajo
                    if random.choice(['7-3', '3-7']) == '7-3':
                        temp_population = random.sample(agreed_players, 7) + random.sample(disagreed_players, 3)
                    else:
                        temp_population = random.sample(agreed_players, 3) + random.sample(disagreed_players, 7)
                    selected_players = random.sample(temp_population, 3)
                
                # Asignar contexto y actualizar contadores
                for player in selected_players:
                    player.participant.vars['context_Tabaco'] = f"Contexto {contexto_seleccionado}"
                    player.participant.vars['group_number_Tabaco'] = group_number_Tabaco
                    player.participant.vars['order_number_Tabaco'] = order_number_Tabaco  # Asignar número de orden
                    order_number_Tabaco += 1
                    remaining_players.remove(player)
                    option_counts[player.antitabaco] -= 1

                group_number_Tabaco += 1
                order_number_Tabaco = 1  # Reiniciar el número de orden para el próximo grupo


                # Recalcular la disponibilidad de jugadores
                option_counts['De acuerdo'] = len([p for p in remaining_players if p.antitabaco == 'De acuerdo'])
                option_counts['En desacuerdo'] = len([p for p in remaining_players if p.antitabaco == 'En desacuerdo'])

            # Inicio de la formación de grupos 'Sin Contexto'
            print("Formando grupos 'Sin Contexto' con los jugadores restantes...")
            while len(remaining_players) >= 3:
                # Selecciona aleatoriamente 3 jugadores de los que quedan
                selected_players = random.sample(remaining_players, 3)
                for player in selected_players:
                    player.participant.vars['context_Tabaco'] = "Sin Contexto"
                    player.participant.vars['group_number_Tabaco'] = group_number_Tabaco
                    # Es importante remover a los jugadores seleccionados de la lista de remaining_players
                    remaining_players = [p for p in remaining_players if p not in selected_players]
                print(f"Grupo {group_number_Tabaco} formado con 'Sin Contexto'.")
                group_number_Tabaco += 1

            # Si después de formar grupos de 3 quedan 1 o 2 jugadores, se les asigna al último grupo 'Sin Contexto'
            if remaining_players:
                for player in remaining_players:
                    player.participant.vars['context_Tabaco'] = "Sin Contexto"
                    player.participant.vars['group_number_Tabaco'] = group_number_Tabaco
                print(f"Jugadores restantes asignados al grupo {group_number_Tabaco} con 'Sin Contexto'.")
                # No incrementamos group_number aquí porque estamos agregando a los jugadores restantes al último grupo formado.

            group.session.vars['groups_formed_Tabaco'] = True
            print("Todos los grupos han sido formados correctamente.")
        
        group.groups_formed_Tabaco = True


class GroupingSyncWaitPage_Tabaco(WaitPage):
    def is_displayed(self):
        return self.round_number == 2

    def after_all_players_arrive(self):
        # Llama al método set_custom_grouping directamente, no como una cadena
        self.subsession.set_custom_grouping_Tabaco()
   

class ShowContext_Tabaco(Page):
    def is_displayed(self):
        return self.round_number == 2

    def vars_for_template(self):
        context_Tabaco = self.participant.vars.get('context_Tabaco', 'Sin Contexto')
        order_number_Tabaco = self.participant.vars.get('order_number_Tabaco', 1)

        if context_Tabaco == "Contexto Alto":
            message_Tabaco = f"""Bienvenido a la segunda parte del experimento. Gracias por la espera, reunimos la información de todas las respuestas de los participantes. Para esta sección te hemos colocado en un grupo con otras dos personas. Van a tomar turnos para responder la siguiente pregunta en frente de los demás: ¿Estás de acuerdo con la nueva ley antitabaco en México?. A cada uno le asignamos un número que representa el orden en el que responderán a la pregunta, el tuyo es el {order_number_Tabaco}.

Creamos el grupo a partir de una población de 10 personas. De estas 10, 7 eligieron “De acuerdo” y 3 eligieron “En desacuerdo" a la pregunta: ¿Estás de acuerdo con la nueva ley antitabaco en México?. Escogimos a cada uno de los integrantes aleatoriamente."""
        elif context_Tabaco == "Contexto Bajo":
            message_Tabaco = f"""Bienvenido a la segunda parte del experimento. Gracias por la espera, reunimos la información de todas las respuestas de los participantes. Para esta sección te hemos colocado en un grupo con otras dos personas. Van a tomar turnos para responder la siguiente pregunta en frente de los demás: ¿Estás de acuerdo con la nueva ley antitabaco en México?. A cada uno le asignamos un número que representa el orden en el que responderán a la pregunta, el tuyo es el {order_number_Tabaco}.

Creamos el grupo tras seleccionar aleatoriamente a una de las dos poblaciones disponibles, cada una con 10 personas, para el presente experimento. La primera población, con una probabilidad del 50%, donde 7 de las personas eligieron “De acuerdo” y 3 eligieron “En desacuerdo” a la pregunta: ¿Estás de acuerdo con la nueva ley antitabaco en México?. La segunda población, con una probabilidad del 50%, donde 3 de las personas eligieron “De acuerdo” y 7 eligieron “En desacuerdo” a la pregunta: ¿Estás de acuerdo con la nueva ley antitabaco en México?. Escogimos a cada uno de los integrantes aleatoriamente."""
        elif context_Tabaco == "Sin Contexto":
            message_Tabaco = f"""Bienvenido a la segunda parte del experimento. Gracias por la espera, reunimos la información de todas las respuestas de los participantes. Para esta sección te hemos colocado en un grupo con otras dos personas. Van a tomar turnos para responder la siguiente pregunta en frente de los demás: ¿Estás de acuerdo con la nueva ley antitabaco en México?. A cada uno le asignamos un número que representa el orden en el que responderán a la pregunta, el tuyo es el {order_number_Tabaco}. Creamos el grupo aleatoriamente."""

        return {
            'context_text_Tabaco': context_Tabaco,
            'message_Tabaco': message_Tabaco,
            'next_button_label': "Continuar"
        }

# Interacción Grupal Tabaco
class AntitabacoQuestion1(Page):
    form_model = 'player'
    form_fields = ['antitabaco_group']

    def is_displayed(self):
        return self.round_number == 2 and self.participant.vars['order_number_Tabaco'] == 1
    
    def vars_for_template(self):
        return dict(next_button_label="Continuar")

    def before_next_page(self, timeout_happened):
        self.group.current_responder = 2

class TabacoWaitForMember1(WaitPage):
    def is_displayed(self):
        return self.round_number == 2
    
    def after_all_players_arrive(self):
        if self.group.current_responder == 2:
            return  # Permite que el miembro 2 avance a su pregunta
        
class TabacoShowResponseMember1(Page):
    def is_displayed(self):
        return self.round_number == 2
    
    def vars_for_template(self):
        member1 = self.group.get_player_by_id(1)
        return {'member1_response': member1.antitabaco_group,
                'next_button_label': "Continuar"}
    
class TabacoQuestionsForMember1(Page):
    form_model = 'player'
    form_fields = ['Tabaco_money_expected2', 'Tabaco_money_expected3', 'Tabaco_money_notexpected2', 'Tabaco_money_notexpected3', 'Tabaco_realtypejueces2', 'Tabaco_realtypejueces3']
    
    def is_displayed(self):
        return self.round_number == 2 and self.participant.vars['order_number_Tabaco'] == 1
    
    def vars_for_template(self):
        return dict(next_button_label="Continuar")

class TabacoDistributeMoneyPage1(Page):
    form_model = 'player'
    form_fields = ['Tabaco_money_to_member1', 'Tabaco_realtypeactor1', 'Tabaco_realtypejuez2', 'Tabaco_realtypejuez3' ]

    def is_displayed(self):
        # Solo se muestra para los miembros 2 y 3
        return self.round_number == 2 and self.participant.vars['order_number_Tabaco'] in [2, 3]
    
    def vars_for_template(self):
        member1 = self.group.get_player_by_id(1)
        return {'member1_response': member1.antitabaco_group,
                'next_button_label': "Continuar"}
    
class TabacoWaitForMoneyDistribution1(WaitPage):
    def is_displayed(self):
        return self.round_number == 2
    
    def after_all_players_arrive(self):
        return  # Esto asegura que todos hayan pasado por DistributeMoneyPage antes de continuar


class AntitabacoQuestion2(Page):
    form_model = 'player'
    form_fields = ['antitabaco_group']
    def is_displayed(self):
        return self.round_number == 2 and self.participant.vars['order_number_Tabaco'] == 2
    def before_next_page(self, timeout_happened):
        self.group.current_responder = 3  # Indica que ahora es el turno del miembro 3
    def vars_for_template(self):
        return dict(next_button_label="Continuar")


class TabacoWaitForMember2(WaitPage):
    def is_displayed(self):
        return self.round_number == 2
    
    def after_all_players_arrive(self):
        if self.group.current_responder == 3:
            return  # Permite que el miembro 3 avance a su pregunta
        
class TabacoShowResponseMember2(Page):
    def is_displayed(self):
        return self.round_number == 2
    
    def vars_for_template(self):
        member2 = self.group.get_player_by_id(2)
        return {'member2_response': member2.antitabaco_group,
                'next_button_label': "Continuar"}
    
class TabacoQuestionsForMember2(Page):
    form_model = 'player'
    form_fields = ['Tabaco_money_expected1', 'Tabaco_money_expected3', 'Tabaco_money_notexpected1', 'Tabaco_money_notexpected3', 'Tabaco_realtypejueces1', 'Tabaco_realtypejueces3']
    
    def is_displayed(self):
        return self.round_number == 2 and self.participant.vars['order_number_Tabaco'] == 2
    
    def vars_for_template(self):
        return dict(next_button_label="Continuar")

class TabacoDistributeMoneyPage2(Page):
    form_model = 'player'
    form_fields = ['Tabaco_money_to_member2', 'Tabaco_realtypeactor2', 'Tabaco_realtypejuez1', 'Tabaco_realtypejuez3' ]

    def is_displayed(self):
        # Solo se muestra para los miembros 1 y 3
        return self.round_number == 2 and self.participant.vars['order_number_Tabaco'] in [1, 3]
    
    def vars_for_template(self):
        member2 = self.group.get_player_by_id(2)
        return {'member2_response': member2.antitabaco_group,
                'next_button_label': "Continuar"}
    
class TabacoWaitForMoneyDistribution2(WaitPage):
    def is_displayed(self):
        return self.round_number == 2
    
    def after_all_players_arrive(self):
        return  # Esto asegura que todos hayan pasado por DistributeMoneyPage antes de continuar

class AntitabacoQuestion3(Page):
    form_model = 'player'
    form_fields = ['antitabaco_group']
    def is_displayed(self):
        return self.round_number == 2 and self.participant.vars['order_number_Tabaco'] == 3
    def before_next_page(self, timeout_happened):
        self.group.current_responder = 4  # Indica que todos han completado
    def vars_for_template(self):
        return dict(next_button_label="Continuar")

class TabacoWaitForMember3(WaitPage):
    def is_displayed(self):
        return self.round_number == 2
    
    def after_all_players_arrive(self):
        if self.group.current_responder == 4:
            return  # Permite que el miembro 3 avance a su pregunta
        
class TabacoShowResponseMember3(Page):
    def is_displayed(self):
        return self.round_number == 2
    
    def vars_for_template(self):
        member3 = self.group.get_player_by_id(3)
        return {'member3_response': member3.antitabaco_group,
                'next_button_label': "Continuar"}
    
class TabacoQuestionsForMember3(Page):
    form_model = 'player'
    form_fields = ['Tabaco_money_expected1', 'Tabaco_money_expected2', 'Tabaco_money_notexpected1', 'Tabaco_money_notexpected2', 'Tabaco_realtypejueces1', 'Tabaco_realtypejueces2']
    
    def is_displayed(self):
        return self.round_number == 2 and self.participant.vars['order_number_Tabaco'] == 3
    
    def vars_for_template(self):
        return dict(next_button_label="Continuar")

class TabacoDistributeMoneyPage3(Page):
    form_model = 'player'
    form_fields = ['Tabaco_money_to_member3', 'Tabaco_realtypeactor3', 'Tabaco_realtypejuez1', 'Tabaco_realtypejuez2' ]

    def is_displayed(self):
        # Solo se muestra para los miembros 1 y 3
        return self.round_number == 2 and self.participant.vars['order_number_Tabaco'] in [1, 2]
    
    def vars_for_template(self):
        member3 = self.group.get_player_by_id(3)
        return {'member3_response': member3.antitabaco_group,
                'next_button_label': "Continuar"}
    
class TabacoWaitForMoneyDistribution3(WaitPage):
    def is_displayed(self):
        return self.round_number == 2
    
    def after_all_players_arrive(self):
        return  # Esto asegura que todos hayan pasado por DistributeMoneyPage antes de continuar

# Formación de grupos para pregunta Arte

class GlobalSyncWaitPage_Arte(WaitPage):
    wait_for_all_groups = True

    def is_displayed(self):
        return self.round_number == 3

    def after_all_players_arrive(self):
        self.session.vars['groups_formed_Arte'] = False
        print("Variables reseteadas, listo para formar grupos para Arte.")
    #Página de Espera
class Forming_Groups_WaitPage_Arte(WaitPage):
    def is_displayed(self):
        return self.round_number == 3
    
    def body_text(self):
        return "Gracias por responder a las preguntas. Por favor espere a la indicación del encargado.<br><br>Favor de esperar a que todos los participantes hayan respondido a las preguntas."

    @staticmethod
    def after_all_players_arrive(group: Group):
        print("Inicio de la formación de grupos para Arte...")
        if not group.session.vars.get('groups_formed_Arte', False):
            players = group.get_players()
            option_counts = {'Sí tiene el mismo virtuosismo': 0, 'No tiene el mismo virtuosismo': 0}
            remaining_players = players.copy()
    
            for p in players:
                # Aquí obtienes el valor de 'arte' desde las variables de participante, asumiendo que fue guardado allí previamente
                arte_value = p.participant.vars.get('arte', '')
                if arte_value:
                    option_counts[arte_value] += 1
                    p.arte = arte_value

            group_number_Arte = 1
            order_number_Arte = 1

            while option_counts['Sí tiene el mismo virtuosismo'] >= 7 and option_counts['No tiene el mismo virtuosismo'] >= 7:
                print(f"Intentando formar un grupo bajo las condiciones actuales... Grupo Número: {group_number_Arte}")
                contexto_seleccionado = random.choice(['Alto', 'Bajo'])
                print(f"Contexto seleccionado: {contexto_seleccionado}")

                agreed_players = [p for p in remaining_players if p.arte == 'Sí tiene el mismo virtuosismo']
                disagreed_players = [p for p in remaining_players if p.arte == 'No tiene el mismo virtuosismo']

                if contexto_seleccionado == 'Alto':
                    # Proceso específico para Contexto Alto
                    temp_population = random.sample(agreed_players, 7) + random.sample(disagreed_players, 3)
                    selected_players = random.sample(temp_population, 3)
                elif contexto_seleccionado == 'Bajo':
                    # Proceso específico para Contexto Bajo
                    if random.choice(['7-3', '3-7']) == '7-3':
                        temp_population = random.sample(agreed_players, 7) + random.sample(disagreed_players, 3)
                    else:
                        temp_population = random.sample(agreed_players, 3) + random.sample(disagreed_players, 7)
                    selected_players = random.sample(temp_population, 3)
                
                # Asignar contexto y actualizar contadores
                for player in selected_players:
                    player.participant.vars['context_Arte'] = f"Contexto {contexto_seleccionado}"
                    player.participant.vars['group_number_Arte'] = group_number_Arte
                    player.participant.vars['order_number_Arte'] = order_number_Arte  # Asignar número de orden
                    order_number_Arte += 1
                    remaining_players.remove(player)
                    option_counts[player.arte] -= 1

                group_number_Arte += 1
                order_number_Arte = 1  # Reiniciar el número de orden para el próximo grupo


                # Recalcular la disponibilidad de jugadores
                option_counts['Sí tiene el mismo virtuosismo'] = len([p for p in remaining_players if p.arte == 'Sí tiene el mismo virtuosismo'])
                option_counts['No tiene el mismo virtuosismo'] = len([p for p in remaining_players if p.arte == 'No tiene el mismo virtuosismo'])

            # Inicio de la formación de grupos 'Sin Contexto'
            print("Formando grupos 'Sin Contexto' con los jugadores restantes...")
            while len(remaining_players) >= 3:
                # Selecciona aleatoriamente 3 jugadores de los que quedan
                selected_players = random.sample(remaining_players, 3)
                for player in selected_players:
                    player.participant.vars['context_Arte'] = "Sin Contexto"
                    player.participant.vars['group_number_Arte'] = group_number_Arte
                    # Es importante remover a los jugadores seleccionados de la lista de remaining_players
                    remaining_players = [p for p in remaining_players if p not in selected_players]
                print(f"Grupo {group_number_Arte} formado con 'Sin Contexto'.")
                group_number_Arte += 1

            # Si después de formar grupos de 3 quedan 1 o 2 jugadores, se les asigna al último grupo 'Sin Contexto'
            if remaining_players:
                for player in remaining_players:
                    player.participant.vars['context_Arte'] = "Sin Contexto"
                    player.participant.vars['group_number_Arte'] = group_number_Arte
                print(f"Jugadores restantes asignados al grupo {group_number_Arte} con 'Sin Contexto'.")
                # No incrementamos group_number aquí porque estamos agregando a los jugadores restantes al último grupo formado.

            group.session.vars['groups_formed_Arte'] = True
            print("Todos los grupos han sido formados correctamente.")
        
        group.groups_formed_Arte = True


class GroupingSyncWaitPage_Arte(WaitPage):
    def is_displayed(self):
        return self.round_number == 3
    
    def after_all_players_arrive(self):
        # Llama al método set_custom_grouping directamente, no como una cadena
        self.subsession.set_custom_grouping_Arte()
   

class ShowContext_Arte(Page):
    def is_displayed(self):
        return self.round_number == 3

    def vars_for_template(self):
        context_Arte = self.participant.vars.get('context_Arte', 'Sin Contexto')
        order_number_Arte = self.participant.vars.get('order_number_Arte', 1)

        if context_Arte == "Contexto Alto":
            message_Arte = f"""Bienvenido a la segunda parte del experimento. Gracias por la espera, reunimos la información de todas las respuestas de los participantes. Para esta sección te hemos colocado en un grupo con otras dos personas. Van a tomar turnos para responder la siguiente pregunta en frente de los demás: ¿El arte que se exhibe en los museos de arte contemporáneo ya no tiene el mismo virtuosismo que el arte en los museos clásicos?. A cada uno le asignamos un número que representa el orden en el que responderán a la pregunta, el tuyo es el {order_number_Arte}.

Creamos el grupo a partir de una población de 10 personas. De estas 10, 7 eligieron “Sí tiene el mismo virtuosismo” y 3 eligieron “No tiene el mismo virtuosismo" a la pregunta: ¿El arte que se exhibe en los museos de arte contemporáneo ya no tiene el mismo virtuosismo que el arte en los museos clásicos?. Escogimos a cada uno de los integrantes aleatoriamente."""
        elif context_Arte == "Contexto Bajo":
            message_Arte = f"""Bienvenido a la segunda parte del experimento. Gracias por la espera, reunimos la información de todas las respuestas de los participantes. Para esta sección te hemos colocado en un grupo con otras dos personas. Van a tomar turnos para responder la siguiente pregunta en frente de los demás: ¿El arte que se exhibe en los museos de arte contemporáneo ya no tiene el mismo virtuosismo que el arte en los museos clásicos?. A cada uno le asignamos un número que representa el orden en el que responderán a la pregunta, el tuyo es el {order_number_Arte}.

Creamos el grupo tras seleccionar aleatoriamente a una de las dos poblaciones disponibles, cada una con 10 personas, para el presente experimento. La primera población, con una probabilidad del 50%, donde 7 de las personas eligieron “Sí tiene el mismo virtuosismo” y 3 eligieron “No tiene el mismo virtuosismo” a la pregunta: ¿El arte que se exhibe en los museos de arte contemporáneo ya no tiene el mismo virtuosismo que el arte en los museos clásicos?. La segunda población, con una probabilidad del 50%, donde 3 de las personas eligieron “Sí tiene el mismo virtuosismo” y 7 eligieron “No tiene el mismo virtuosismo” a la pregunta: ¿El arte que se exhibe en los museos de arte contemporáneo ya no tiene el mismo virtuosismo que el arte en los museos clásicos?. Escogimos a cada uno de los integrantes aleatoriamente."""
        elif context_Arte == "Sin Contexto":
            message_Arte = f"""Bienvenido a la segunda parte del experimento. Gracias por la espera, reunimos la información de todas las respuestas de los participantes. Para esta sección te hemos colocado en un grupo con otras dos personas. Van a tomar turnos para responder la siguiente pregunta en frente de los demás: ¿El arte que se exhibe en los museos de arte contemporáneo ya no tiene el mismo virtuosismo que el arte en los museos clásicos?. A cada uno le asignamos un número que representa el orden en el que responderán a la pregunta, el tuyo es el {order_number_Arte}. Creamos el grupo aleatoriamente."""

        return {
            'context_text_Arte': context_Arte,
            'message_Arte': message_Arte,
            'next_button_label': "Continuar"
        }

# Interacción Grupal Arte
    
class ArteQuestion1(Page):
    form_model = 'player'
    form_fields = ['arte_group']

    def is_displayed(self):
        return self.round_number == 3 and self.participant.vars['order_number_Arte'] == 1
    
    def vars_for_template(self):
        return dict(next_button_label="Continuar")

    def before_next_page(self, timeout_happened):
        self.group.current_responder = 2

class ArteWaitForMember1(WaitPage):
    def is_displayed(self):
        return self.round_number == 3
    
    def after_all_players_arrive(self):
        if self.group.current_responder == 2:
            return  # Permite que el miembro 2 avance a su pregunta
        
class ArteShowResponseMember1(Page):
    def is_displayed(self):
        return self.round_number == 3
    
    def vars_for_template(self):
        member1 = self.group.get_player_by_id(1)
        return {'member1_response': member1.arte_group,
                'next_button_label': "Continuar"}
    
class ArteQuestionsForMember1(Page):
    form_model = 'player'
    form_fields = ['Arte_money_expected2', 'Arte_money_expected3', 'Arte_money_notexpected2', 'Arte_money_notexpected3', 'Arte_realtypejueces2', 'Arte_realtypejueces3']
    
    def is_displayed(self):
        return self.round_number == 3 and self.participant.vars['order_number_Arte'] == 1
    
    def vars_for_template(self):
        return dict(next_button_label="Continuar")

class ArteDistributeMoneyPage1(Page):
    form_model = 'player'
    form_fields = ['Arte_money_to_member1', 'Arte_realtypeactor1', 'Arte_realtypejuez2', 'Arte_realtypejuez3' ]

    def is_displayed(self):
        # Solo se muestra para los miembros 2 y 3
        return self.round_number == 3 and self.participant.vars['order_number_Arte'] in [2, 3]
    
    def vars_for_template(self):
        member1 = self.group.get_player_by_id(1)
        return {'member1_response': member1.arte_group,
                'next_button_label': "Continuar"}
    
class ArteWaitForMoneyDistribution1(WaitPage):
    def is_displayed(self):
        return self.round_number == 3
    
    def after_all_players_arrive(self):
        return  # Esto asegura que todos hayan pasado por DistributeMoneyPage antes de continuar


class ArteQuestion2(Page):
    form_model = 'player'
    form_fields = ['arte_group']
    def is_displayed(self):
        return self.round_number == 3 and self.participant.vars['order_number_Arte'] == 2
    def before_next_page(self, timeout_happened):
        self.group.current_responder = 3  # Indica que ahora es el turno del miembro 3
    def vars_for_template(self):
        return dict(next_button_label="Continuar")


class ArteWaitForMember2(WaitPage):
    def is_displayed(self):
        return self.round_number == 3
    
    def after_all_players_arrive(self):
        if self.group.current_responder == 3:
            return  # Permite que el miembro 3 avance a su pregunta
        
class ArteShowResponseMember2(Page):
    def is_displayed(self):
        return self.round_number == 3
    
    def vars_for_template(self):
        member2 = self.group.get_player_by_id(2)
        return {'member2_response': member2.arte_group,
                'next_button_label': "Continuar"}
    
class ArteQuestionsForMember2(Page):
    form_model = 'player'
    form_fields = ['Arte_money_expected1', 'Arte_money_expected3', 'Arte_money_notexpected1', 'Arte_money_notexpected3', 'Arte_realtypejueces1', 'Arte_realtypejueces3']
    
    def is_displayed(self):
        return self.round_number == 3 and self.participant.vars['order_number_Arte'] == 2
    
    def vars_for_template(self):
        return dict(next_button_label="Continuar")

class ArteDistributeMoneyPage2(Page):
    form_model = 'player'
    form_fields = ['Arte_money_to_member2', 'Arte_realtypeactor2', 'Arte_realtypejuez1', 'Arte_realtypejuez3' ]

    def is_displayed(self):
        # Solo se muestra para los miembros 1 y 3
        return self.round_number == 3 and self.participant.vars['order_number_Arte'] in [1, 3]
    
    def vars_for_template(self):
        member2 = self.group.get_player_by_id(2)
        return {'member2_response': member2.arte_group,
                'next_button_label': "Continuar"}
    
class ArteWaitForMoneyDistribution2(WaitPage):
    def is_displayed(self):
        return self.round_number == 3
    
    def after_all_players_arrive(self):
        return  # Esto asegura que todos hayan pasado por DistributeMoneyPage antes de continuar

class ArteQuestion3(Page):
    form_model = 'player'
    form_fields = ['arte_group']
    def is_displayed(self):
        return self.round_number == 3 and self.participant.vars['order_number_Arte'] == 3
    def before_next_page(self, timeout_happened):
        self.group.current_responder = 4  # Indica que todos han completado
    def vars_for_template(self):
        return dict(next_button_label="Continuar")

class ArteWaitForMember3(WaitPage):
    def is_displayed(self):
        return self.round_number == 3
    
    def after_all_players_arrive(self):
        if self.group.current_responder == 4:
            return  # Permite que el miembro 3 avance a su pregunta
        
class ArteShowResponseMember3(Page):
    def is_displayed(self):
        return self.round_number == 3
    
    def vars_for_template(self):
        member3 = self.group.get_player_by_id(3)
        return {'member3_response': member3.arte_group,
                'next_button_label': "Continuar"}
    
class ArteQuestionsForMember3(Page):
    form_model = 'player'
    form_fields = ['Arte_money_expected1', 'Arte_money_expected2', 'Arte_money_notexpected1', 'Arte_money_notexpected2', 'Arte_realtypejueces1', 'Arte_realtypejueces2']
    
    def is_displayed(self):
        return self.round_number == 3 and self.participant.vars['order_number_Arte'] == 3
    
    def vars_for_template(self):
        return dict(next_button_label="Continuar")

class ArteDistributeMoneyPage3(Page):
    form_model = 'player'
    form_fields = ['Arte_money_to_member3', 'Arte_realtypeactor3', 'Arte_realtypejuez1', 'Arte_realtypejuez2' ]

    def is_displayed(self):
        # Solo se muestra para los miembros 1 y 3
        return self.round_number == 3 and self.participant.vars['order_number_Arte'] in [1, 2]
    
    def vars_for_template(self):
        member3 = self.group.get_player_by_id(3)
        return {'member3_response': member3.arte_group,
                'next_button_label': "Continuar"}
    
class ArteWaitForMoneyDistribution3(WaitPage):
    def is_displayed(self):
        return self.round_number == 3
    
    def after_all_players_arrive(self):
        return  # Esto asegura que todos hayan pasado por DistributeMoneyPage antes de continuar

# Formación de grupos para pregunta Violencia

class GlobalSyncWaitPage_Violencia(WaitPage):
    wait_for_all_groups = True

    def is_displayed(self):
        return self.round_number == 4

    def after_all_players_arrive(self):
        self.session.vars['groups_formed_Violencia'] = False
        print("Variables reseteadas, listo para formar grupos para Violencia.")
    #Página de Espera
class Forming_Groups_WaitPage_Violencia(WaitPage):
    def is_displayed(self):
        return self.round_number == 4
    
    def body_text(self):
        return "Gracias por responder a las preguntas. Por favor espere a la indicación del encargado.<br><br>Favor de esperar a que todos los participantes hayan respondido a las preguntas."

    @staticmethod
    def after_all_players_arrive(group: Group):
        print("Inicio de la formación de grupos para Violencia...")
        if not group.session.vars.get('groups_formed_Violencia', False):
            players = group.get_players()
            option_counts = {'De acuerdo': 0, 'En desacuerdo': 0}
            remaining_players = players.copy()
    
            for p in players:
                # Aquí obtienes el valor de 'violencia' desde las variables de participante, asumiendo que fue guardado allí previamente
                violencia_value = p.participant.vars.get('violencia', '')
                if violencia_value:
                    option_counts[violencia_value] += 1
                    p.violencia = violencia_value

            group_number_Violencia = 1
            order_number_Violencia = 1

            while option_counts['De acuerdo'] >= 7 and option_counts['En desacuerdo'] >= 7:
                print(f"Intentando formar un grupo bajo las condiciones actuales... Grupo Número: {group_number_Violencia}")
                contexto_seleccionado = random.choice(['Alto', 'Bajo'])
                print(f"Contexto seleccionado: {contexto_seleccionado}")

                agreed_players = [p for p in remaining_players if p.violencia == 'De acuerdo']
                disagreed_players = [p for p in remaining_players if p.violencia == 'En desacuerdo']

                if contexto_seleccionado == 'Alto':
                    # Proceso específico para Contexto Alto
                    temp_population = random.sample(agreed_players, 7) + random.sample(disagreed_players, 3)
                    selected_players = random.sample(temp_population, 3)
                elif contexto_seleccionado == 'Bajo':
                    # Proceso específico para Contexto Bajo
                    if random.choice(['7-3', '3-7']) == '7-3':
                        temp_population = random.sample(agreed_players, 7) + random.sample(disagreed_players, 3)
                    else:
                        temp_population = random.sample(agreed_players, 3) + random.sample(disagreed_players, 7)
                    selected_players = random.sample(temp_population, 3)
                
                # Asignar contexto y actualizar contadores
                for player in selected_players:
                    player.participant.vars['context_Violencia'] = f"Contexto {contexto_seleccionado}"
                    player.participant.vars['group_number_Violencia'] = group_number_Violencia
                    player.participant.vars['order_number_Violencia'] = order_number_Violencia  # Asignar número de orden
                    order_number_Violencia += 1
                    remaining_players.remove(player)
                    option_counts[player.violencia] -= 1

                group_number_Violencia += 1
                order_number_Violencia = 1  # Reiniciar el número de orden para el próximo grupo


                # Recalcular la disponibilidad de jugadores
                option_counts['De acuerdo'] = len([p for p in remaining_players if p.violencia == 'De acuerdo'])
                option_counts['En desacuerdo'] = len([p for p in remaining_players if p.violencia == 'En desacuerdo'])

            # Inicio de la formación de grupos 'Sin Contexto'
            print("Formando grupos 'Sin Contexto' con los jugadores restantes...")
            while len(remaining_players) >= 3:
                # Selecciona aleatoriamente 3 jugadores de los que quedan
                selected_players = random.sample(remaining_players, 3)
                for player in selected_players:
                    player.participant.vars['context_Violencia'] = "Sin Contexto"
                    player.participant.vars['group_number_Violencia'] = group_number_Violencia
                    # Es importante remover a los jugadores seleccionados de la lista de remaining_players
                    remaining_players = [p for p in remaining_players if p not in selected_players]
                print(f"Grupo {group_number_Violencia} formado con 'Sin Contexto'.")
                group_number_Violencia += 1

            # Si después de formar grupos de 3 quedan 1 o 2 jugadores, se les asigna al último grupo 'Sin Contexto'
            if remaining_players:
                for player in remaining_players:
                    player.participant.vars['context_Violencia'] = "Sin Contexto"
                    player.participant.vars['group_number_Violencia'] = group_number_Violencia
                print(f"Jugadores restantes asignados al grupo {group_number_Violencia} con 'Sin Contexto'.")
                # No incrementamos group_number aquí porque estamos agregando a los jugadores restantes al último grupo formado.

            group.session.vars['groups_formed_Violencia'] = True
            print("Todos los grupos han sido formados correctamente.")
        
        group.groups_formed_Violencia = True


class GroupingSyncWaitPage_Violencia(WaitPage):
    def is_displayed(self):
        return self.round_number == 4
    
    def after_all_players_arrive(self):
        # Llama al método set_custom_grouping directamente, no como una cadena
        self.subsession.set_custom_grouping_Violencia()
   

class ShowContext_Violencia(Page):
    def is_displayed(self):
        return self.round_number == 4

    def vars_for_template(self):
        context_Violencia = self.participant.vars.get('context_Violencia', 'Sin Contexto')
        order_number_Violencia = self.participant.vars.get('order_number_Violencia', 1)

        if context_Violencia == "Contexto Alto":
            message_Violencia = f"""Bienvenido a la segunda parte del experimento. Gracias por la espera, reunimos la información de todas las respuestas de los participantes. Para esta sección te hemos colocado en un grupo con otras dos personas. Van a tomar turnos para responder la siguiente pregunta en frente de los demás: ¿Estás de acuerdo con la frase “no hay paz sin la violencia”?. A cada uno le asignamos un número que representa el orden en el que responderán a la pregunta, el tuyo es el {order_number_Violencia}.

Creamos el grupo a partir de una población de 10 personas. De estas 10, 7 eligieron “De acuerdo” y 3 eligieron “En desacuerdo" a la pregunta: ¿Estás de acuerdo con la frase “no hay paz sin la violencia”?. Escogimos a cada uno de los integrantes aleatoriamente."""
        elif context_Violencia == "Contexto Bajo":
            message_Violencia = f"""Bienvenido a la segunda parte del experimento. Gracias por la espera, reunimos la información de todas las respuestas de los participantes. Para esta sección te hemos colocado en un grupo con otras dos personas. Van a tomar turnos para responder la siguiente pregunta en frente de los demás: ¿Estás de acuerdo con la frase “no hay paz sin la violencia”?. A cada uno le asignamos un número que representa el orden en el que responderán a la pregunta, el tuyo es el {order_number_Violencia}.

Creamos el grupo tras seleccionar aleatoriamente a una de las dos poblaciones disponibles, cada una con 10 personas, para el presente experimento. La primera población, con una probabilidad del 50%, donde 7 de las personas eligieron “De acuerdo” y 3 eligieron “En desacuerdo” a la pregunta: ¿Estás de acuerdo con la frase “no hay paz sin la violencia”?. La segunda población, con una probabilidad del 50%, donde 3 de las personas eligieron “De acuerdo” y 7 eligieron “En desacuerdo” a la pregunta: ¿Estás de acuerdo con la frase “no hay paz sin la violencia”?. Escogimos a cada uno de los integrantes aleatoriamente."""
        elif context_Violencia == "Sin Contexto":
            message_Violencia = f"""Bienvenido a la segunda parte del experimento. Gracias por la espera, reunimos la información de todas las respuestas de los participantes. Para esta sección te hemos colocado en un grupo con otras dos personas. Van a tomar turnos para responder la siguiente pregunta en frente de los demás: ¿Estás de acuerdo con la frase “no hay paz sin la violencia”?. A cada uno le asignamos un número que representa el orden en el que responderán a la pregunta, el tuyo es el {order_number_Violencia}. Creamos el grupo aleatoriamente."""

        return {
            'context_text_Violencia': context_Violencia,
            'message_Violencia': message_Violencia,
            'next_button_label': "Continuar"
        }
    
# Interacción Grupal Violencia
    
class ViolenciaQuestion1(Page):
    form_model = 'player'
    form_fields = ['violencia_group']

    def is_displayed(self):
        return self.round_number == 4 and self.participant.vars['order_number_Violencia'] == 1
    
    def vars_for_template(self):
        return dict(next_button_label="Continuar")

    def before_next_page(self, timeout_happened):
        self.group.current_responder = 2

class ViolenciaWaitForMember1(WaitPage):
    def is_displayed(self):
        return self.round_number == 4
    
    def after_all_players_arrive(self):
        if self.group.current_responder == 2:
            return  # Permite que el miembro 2 avance a su pregunta
        
class ViolenciaShowResponseMember1(Page):
    def is_displayed(self):
        return self.round_number == 4
    
    def vars_for_template(self):
        member1 = self.group.get_player_by_id(1)
        return {'member1_response': member1.violencia_group,
                'next_button_label': "Continuar"}
    
class ViolenciaQuestionsForMember1(Page):
    form_model = 'player'
    form_fields = ['Violencia_money_expected2', 'Violencia_money_expected3', 'Violencia_money_notexpected2', 'Violencia_money_notexpected3', 'Violencia_realtypejueces2', 'Violencia_realtypejueces3']
    
    def is_displayed(self):
        return self.round_number == 4 and self.participant.vars['order_number_Violencia'] == 1
    
    def vars_for_template(self):
        return dict(next_button_label="Continuar")

class ViolenciaDistributeMoneyPage1(Page):
    form_model = 'player'
    form_fields = ['Violencia_money_to_member1', 'Violencia_realtypeactor1', 'Violencia_realtypejuez2', 'Violencia_realtypejuez3' ]

    def is_displayed(self):
        # Solo se muestra para los miembros 2 y 3
        return self.round_number == 4 and self.participant.vars['order_number_Violencia'] in [2, 3]
    
    def vars_for_template(self):
        member1 = self.group.get_player_by_id(1)
        return {'member1_response': member1.violencia_group,
                'next_button_label': "Continuar"}
    
class ViolenciaWaitForMoneyDistribution1(WaitPage):
    def is_displayed(self):
        return self.round_number == 4
    
    def after_all_players_arrive(self):
        return  # Esto asegura que todos hayan pasado por DistributeMoneyPage antes de continuar


class ViolenciaQuestion2(Page):
    form_model = 'player'
    form_fields = ['violencia_group']
    def is_displayed(self):
        return self.round_number == 4 and self.participant.vars['order_number_Violencia'] == 2
    def before_next_page(self, timeout_happened):
        self.group.current_responder = 3  # Indica que ahora es el turno del miembro 3
    def vars_for_template(self):
        return dict(next_button_label="Continuar")


class ViolenciaWaitForMember2(WaitPage):
    def is_displayed(self):
        return self.round_number == 4
    
    def after_all_players_arrive(self):
        if self.group.current_responder == 3:
            return  # Permite que el miembro 3 avance a su pregunta
        
class ViolenciaShowResponseMember2(Page):
    def is_displayed(self):
        return self.round_number == 4
    
    def vars_for_template(self):
        member2 = self.group.get_player_by_id(2)
        return {'member2_response': member2.violencia_group,
                'next_button_label': "Continuar"}
    
class ViolenciaQuestionsForMember2(Page):
    form_model = 'player'
    form_fields = ['Violencia_money_expected1', 'Violencia_money_expected3', 'Violencia_money_notexpected1', 'Violencia_money_notexpected3', 'Violencia_realtypejueces1', 'Violencia_realtypejueces3']
    
    def is_displayed(self):
        return self.round_number == 4 and self.participant.vars['order_number_Violencia'] == 2
    
    def vars_for_template(self):
        return dict(next_button_label="Continuar")

class ViolenciaDistributeMoneyPage2(Page):
    form_model = 'player'
    form_fields = ['Violencia_money_to_member2', 'Violencia_realtypeactor2', 'Violencia_realtypejuez1', 'Violencia_realtypejuez3' ]

    def is_displayed(self):
        # Solo se muestra para los miembros 1 y 3
        return self.round_number == 4 and self.participant.vars['order_number_Violencia'] in [1, 3]
    
    def vars_for_template(self):
        member2 = self.group.get_player_by_id(2)
        return {'member2_response': member2.violencia_group,
                'next_button_label': "Continuar"}
    
class ViolenciaWaitForMoneyDistribution2(WaitPage):
    def is_displayed(self):
        return self.round_number == 4
    
    def after_all_players_arrive(self):
        return  # Esto asegura que todos hayan pasado por DistributeMoneyPage antes de continuar

class ViolenciaQuestion3(Page):
    form_model = 'player'
    form_fields = ['violencia_group']
    def is_displayed(self):
        return self.round_number == 4 and self.participant.vars['order_number_Violencia'] == 3
    def before_next_page(self, timeout_happened):
        self.group.current_responder = 4  # Indica que todos han completado
    def vars_for_template(self):
        return dict(next_button_label="Continuar")

class ViolenciaWaitForMember3(WaitPage):
    def is_displayed(self):
        return self.round_number == 4
    
    def after_all_players_arrive(self):
        if self.group.current_responder == 4:
            return  # Permite que el miembro 3 avance a su pregunta
        
class ViolenciaShowResponseMember3(Page):
    def is_displayed(self):
        return self.round_number == 4
    
    def vars_for_template(self):
        member3 = self.group.get_player_by_id(3)
        return {'member3_response': member3.violencia_group,
                'next_button_label': "Continuar"}
    
class ViolenciaQuestionsForMember3(Page):
    form_model = 'player'
    form_fields = ['Violencia_money_expected1', 'Violencia_money_expected2', 'Violencia_money_notexpected1', 'Violencia_money_notexpected2', 'Violencia_realtypejueces1', 'Violencia_realtypejueces2']
    
    def is_displayed(self):
        return self.round_number == 4 and self.participant.vars['order_number_Violencia'] == 3
    
    def vars_for_template(self):
        return dict(next_button_label="Continuar")

class ViolenciaDistributeMoneyPage3(Page):
    form_model = 'player'
    form_fields = ['Violencia_money_to_member3', 'Violencia_realtypeactor3', 'Violencia_realtypejuez1', 'Violencia_realtypejuez2' ]

    def is_displayed(self):
        # Solo se muestra para los miembros 1 y 3
        return self.round_number == 4 and self.participant.vars['order_number_Violencia'] in [1, 2]
    
    def vars_for_template(self):
        member3 = self.group.get_player_by_id(3)
        return {'member3_response': member3.violencia_group,
                'next_button_label': "Continuar"}
    
class ViolenciaWaitForMoneyDistribution3(WaitPage):
    def is_displayed(self):
        return self.round_number == 4
    
    def after_all_players_arrive(self):
        return  # Esto asegura que todos hayan pasado por DistributeMoneyPage antes de continuar

# Formación de grupos para pregunta Crisis

class GlobalSyncWaitPage_Crisis(WaitPage):
    wait_for_all_groups = True

    def is_displayed(self):
        return self.round_number == 5

    def after_all_players_arrive(self):
        self.session.vars['groups_formed_Crisis'] = False
        print("Variables reseteadas, listo para formar grupos para Crisis.")
    #Página de Espera
class Forming_Groups_WaitPage_Crisis(WaitPage):
    def is_displayed(self):
        return self.round_number == 5
    
    def body_text(self):
        return "Gracias por responder a las preguntas. Por favor espere a la indicación del encargado.<br><br>Favor de esperar a que todos los participantes hayan respondido a las preguntas."

    @staticmethod
    def after_all_players_arrive(group: Group):
        print("Inicio de la formación de grupos para Crisis...")
        if not group.session.vars.get('groups_formed_Crisis', False):
            players = group.get_players()
            option_counts = {'Crisis climática': 0, 'La pobreza extrema': 0}
            remaining_players = players.copy()
    
            for p in players:
                # Aquí obtienes el valor de 'crisis' desde las variables de participante, asumiendo que fue guardado allí previamente
                crisis_value = p.participant.vars.get('crisis', '')
                if crisis_value:
                    option_counts[crisis_value] += 1
                    p.crisis = crisis_value

            group_number_Crisis = 1
            order_number_Crisis = 1

            while option_counts['Crisis climática'] >= 7 and option_counts['La pobreza extrema'] >= 7:
                print(f"Intentando formar un grupo bajo las condiciones actuales... Grupo Número: {group_number_Crisis}")
                contexto_seleccionado = random.choice(['Alto', 'Bajo'])
                print(f"Contexto seleccionado: {contexto_seleccionado}")

                agreed_players = [p for p in remaining_players if p.crisis == 'Crisis climática']
                disagreed_players = [p for p in remaining_players if p.crisis == 'La pobreza extrema']

                if contexto_seleccionado == 'Alto':
                    # Proceso específico para Contexto Alto
                    temp_population = random.sample(agreed_players, 7) + random.sample(disagreed_players, 3)
                    selected_players = random.sample(temp_population, 3)
                elif contexto_seleccionado == 'Bajo':
                    # Proceso específico para Contexto Bajo
                    if random.choice(['7-3', '3-7']) == '7-3':
                        temp_population = random.sample(agreed_players, 7) + random.sample(disagreed_players, 3)
                    else:
                        temp_population = random.sample(agreed_players, 3) + random.sample(disagreed_players, 7)
                    selected_players = random.sample(temp_population, 3)
                
                # Asignar contexto y actualizar contadores
                for player in selected_players:
                    player.participant.vars['context_Crisis'] = f"Contexto {contexto_seleccionado}"
                    player.participant.vars['group_number_Crisis'] = group_number_Crisis
                    player.participant.vars['order_number_Crisis'] = order_number_Crisis  # Asignar número de orden
                    order_number_Crisis += 1
                    remaining_players.remove(player)
                    option_counts[player.crisis] -= 1

                group_number_Crisis += 1
                order_number_Crisis = 1  # Reiniciar el número de orden para el próximo grupo


                # Recalcular la disponibilidad de jugadores
                option_counts['Crisis climática'] = len([p for p in remaining_players if p.crisis == 'Crisis climática'])
                option_counts['La pobreza extrema'] = len([p for p in remaining_players if p.crisis == 'La pobreza extrema'])

            # Inicio de la formación de grupos 'Sin Contexto'
            print("Formando grupos 'Sin Contexto' con los jugadores restantes...")
            while len(remaining_players) >= 3:
                # Selecciona aleatoriamente 3 jugadores de los que quedan
                selected_players = random.sample(remaining_players, 3)
                for player in selected_players:
                    player.participant.vars['context_Crisis'] = "Sin Contexto"
                    player.participant.vars['group_number_Crisis'] = group_number_Crisis
                    # Es importante remover a los jugadores seleccionados de la lista de remaining_players
                    remaining_players = [p for p in remaining_players if p not in selected_players]
                print(f"Grupo {group_number_Crisis} formado con 'Sin Contexto'.")
                group_number_Crisis += 1

            # Si después de formar grupos de 3 quedan 1 o 2 jugadores, se les asigna al último grupo 'Sin Contexto'
            if remaining_players:
                for player in remaining_players:
                    player.participant.vars['context_Crisis'] = "Sin Contexto"
                    player.participant.vars['group_number_Crisis'] = group_number_Crisis
                print(f"Jugadores restantes asignados al grupo {group_number_Crisis} con 'Sin Contexto'.")
                # No incrementamos group_number aquí porque estamos agregando a los jugadores restantes al último grupo formado.

            group.session.vars['groups_formed_Crisis'] = True
            print("Todos los grupos han sido formados correctamente.")
        
        group.groups_formed_Crisis = True


class GroupingSyncWaitPage_Crisis(WaitPage):
    def is_displayed(self):
        return self.round_number == 5
    
    def after_all_players_arrive(self):
        # Llama al método set_custom_grouping directamente, no como una cadena
        self.subsession.set_custom_grouping_Crisis()
   

class ShowContext_Crisis(Page):
    def is_displayed(self):
        return self.round_number == 5

    def vars_for_template(self):
        context_Crisis = self.participant.vars.get('context_Crisis', 'Sin Contexto')
        order_number_Crisis = self.participant.vars.get('order_number_Crisis', 1)

        if context_Crisis == "Contexto Alto":
            message_Crisis = f"""Bienvenido a la segunda parte del experimento. Gracias por la espera, reunimos la información de todas las respuestas de los participantes. Para esta sección te hemos colocado en un grupo con otras dos personas. Van a tomar turnos para responder la siguiente pregunta en frente de los demás: ¿Qué es más importante, afrontar la crisis climática o terminar la pobreza extrema en México?. A cada uno le asignamos un número que representa el orden en el que responderán a la pregunta, el tuyo es el {order_number_Crisis}.

Creamos el grupo a partir de una población de 10 personas. De estas 10, 7 eligieron “Crisis climática” y 3 eligieron “La pobreza extrema" a la pregunta: ¿Qué es más importante, afrontar la crisis climática o terminar la pobreza extrema en México?. Escogimos a cada uno de los integrantes aleatoriamente."""
        elif context_Crisis == "Contexto Bajo":
            message_Crisis = f"""Bienvenido a la segunda parte del experimento. Gracias por la espera, reunimos la información de todas las respuestas de los participantes. Para esta sección te hemos colocado en un grupo con otras dos personas. Van a tomar turnos para responder la siguiente pregunta en frente de los demás: ¿Qué es más importante, afrontar la crisis climática o terminar la pobreza extrema en México?. A cada uno le asignamos un número que representa el orden en el que responderán a la pregunta, el tuyo es el {order_number_Crisis}.

Creamos el grupo tras seleccionar aleatoriamente a una de las dos poblaciones disponibles, cada una con 10 personas, para el presente experimento. La primera población, con una probabilidad del 50%, donde 7 de las personas eligieron “Crisis climática” y 3 eligieron “La pobreza extrema” a la pregunta: ¿Qué es más importante, afrontar la crisis climática o terminar la pobreza extrema en México?. La segunda población, con una probabilidad del 50%, donde 3 de las personas eligieron “Crisis climática” y 7 eligieron “La pobreza extrema” a la pregunta: ¿Qué es más importante, afrontar la crisis climática o terminar la pobreza extrema en México?. Escogimos a cada uno de los integrantes aleatoriamente."""
        elif context_Crisis == "Sin Contexto":
            message_Crisis = f"""Bienvenido a la segunda parte del experimento. Gracias por la espera, reunimos la información de todas las respuestas de los participantes. Para esta sección te hemos colocado en un grupo con otras dos personas. Van a tomar turnos para responder la siguiente pregunta en frente de los demás: ¿Qué es más importante, afrontar la crisis climática o terminar la pobreza extrema en México?. A cada uno le asignamos un número que representa el orden en el que responderán a la pregunta, el tuyo es el {order_number_Crisis}. Creamos el grupo aleatoriamente."""

        return {
            'context_text_Crisis': context_Crisis,
            'message_Crisis': message_Crisis,
            'next_button_label': "Continuar"
        }

# Interacción Grupal Crisis
    
class CrisisQuestion1(Page):
    form_model = 'player'
    form_fields = ['crisis_group']

    def is_displayed(self):
        return self.round_number == 5 and self.participant.vars['order_number_Crisis'] == 1
    
    def vars_for_template(self):
        return dict(next_button_label="Continuar")

    def before_next_page(self, timeout_happened):
        self.group.current_responder = 2

class CrisisWaitForMember1(WaitPage):
    def is_displayed(self):
        return self.round_number == 5
    
    def after_all_players_arrive(self):
        if self.group.current_responder == 2:
            return  # Permite que el miembro 2 avance a su pregunta
        
class CrisisShowResponseMember1(Page):
    def is_displayed(self):
        return self.round_number == 5
    
    def vars_for_template(self):
        member1 = self.group.get_player_by_id(1)
        return {'member1_response': member1.crisis_group,
                'next_button_label': "Continuar"}
    
class CrisisQuestionsForMember1(Page):
    form_model = 'player'
    form_fields = ['Crisis_money_expected2', 'Crisis_money_expected3', 'Crisis_money_notexpected2', 'Crisis_money_notexpected3', 'Crisis_realtypejueces2', 'Crisis_realtypejueces3']
    
    def is_displayed(self):
        return self.round_number == 5 and self.participant.vars['order_number_Crisis'] == 1
    
    def vars_for_template(self):
        return dict(next_button_label="Continuar")

class CrisisDistributeMoneyPage1(Page):
    form_model = 'player'
    form_fields = ['Crisis_money_to_member1', 'Crisis_realtypeactor1', 'Crisis_realtypejuez2', 'Crisis_realtypejuez3' ]

    def is_displayed(self):
        # Solo se muestra para los miembros 2 y 3
        return self.round_number == 5 and self.participant.vars['order_number_Crisis'] in [2, 3]
    
    def vars_for_template(self):
        member1 = self.group.get_player_by_id(1)
        return {'member1_response': member1.crisis_group,
                'next_button_label': "Continuar"}
    
class CrisisWaitForMoneyDistribution1(WaitPage):
    def is_displayed(self):
        return self.round_number == 5
    
    def after_all_players_arrive(self):
        return  # Esto asegura que todos hayan pasado por DistributeMoneyPage antes de continuar


class CrisisQuestion2(Page):
    form_model = 'player'
    form_fields = ['crisis_group']
    def is_displayed(self):
        return self.round_number == 5 and self.participant.vars['order_number_Crisis'] == 2
    def before_next_page(self, timeout_happened):
        self.group.current_responder = 3  # Indica que ahora es el turno del miembro 3
    def vars_for_template(self):
        return dict(next_button_label="Continuar")


class CrisisWaitForMember2(WaitPage):
    def is_displayed(self):
        return self.round_number == 5
    
    def after_all_players_arrive(self):
        if self.group.current_responder == 3:
            return  # Permite que el miembro 3 avance a su pregunta
        
class CrisisShowResponseMember2(Page):
    def is_displayed(self):
        return self.round_number == 5
    
    def vars_for_template(self):
        member2 = self.group.get_player_by_id(2)
        return {'member2_response': member2.crisis_group,
                'next_button_label': "Continuar"}
    
class CrisisQuestionsForMember2(Page):
    form_model = 'player'
    form_fields = ['Crisis_money_expected1', 'Crisis_money_expected3', 'Crisis_money_notexpected1', 'Crisis_money_notexpected3', 'Crisis_realtypejueces1', 'Crisis_realtypejueces3']
    
    def is_displayed(self):
        return self.round_number == 5 and self.participant.vars['order_number_Crisis'] == 2
    
    def vars_for_template(self):
        return dict(next_button_label="Continuar")

class CrisisDistributeMoneyPage2(Page):
    form_model = 'player'
    form_fields = ['Crisis_money_to_member2', 'Crisis_realtypeactor2', 'Crisis_realtypejuez1', 'Crisis_realtypejuez3' ]

    def is_displayed(self):
        # Solo se muestra para los miembros 1 y 3
        return self.round_number == 5 and self.participant.vars['order_number_Crisis'] in [1, 3]
    
    def vars_for_template(self):
        member2 = self.group.get_player_by_id(2)
        return {'member2_response': member2.crisis_group,
                'next_button_label': "Continuar"}
    
class CrisisWaitForMoneyDistribution2(WaitPage):
    def is_displayed(self):
        return self.round_number == 5
    
    def after_all_players_arrive(self):
        return  # Esto asegura que todos hayan pasado por DistributeMoneyPage antes de continuar

class CrisisQuestion3(Page):
    form_model = 'player'
    form_fields = ['crisis_group']
    def is_displayed(self):
        return self.round_number == 5 and self.participant.vars['order_number_Crisis'] == 3
    def before_next_page(self, timeout_happened):
        self.group.current_responder = 4  # Indica que todos han completado
    def vars_for_template(self):
        return dict(next_button_label="Continuar")

class CrisisWaitForMember3(WaitPage):
    def is_displayed(self):
        return self.round_number == 5
    
    def after_all_players_arrive(self):
        if self.group.current_responder == 4:
            return  # Permite que el miembro 3 avance a su pregunta
        
class CrisisShowResponseMember3(Page):
    def is_displayed(self):
        return self.round_number == 5
    
    def vars_for_template(self):
        member3 = self.group.get_player_by_id(3)
        return {'member3_response': member3.crisis_group,
                'next_button_label': "Continuar"}
    
class CrisisQuestionsForMember3(Page):
    form_model = 'player'
    form_fields = ['Crisis_money_expected1', 'Crisis_money_expected2', 'Crisis_money_notexpected1', 'Crisis_money_notexpected2', 'Crisis_realtypejueces1', 'Crisis_realtypejueces2']
    
    def is_displayed(self):
        return self.round_number == 5 and self.participant.vars['order_number_Crisis'] == 3
    
    def vars_for_template(self):
        return dict(next_button_label="Continuar")
    
class CrisisDistributeMoneyPage3(Page):
    form_model = 'player'
    form_fields = ['Crisis_money_to_member3', 'Crisis_realtypeactor3', 'Crisis_realtypejuez1', 'Crisis_realtypejuez2' ]

    def is_displayed(self):
        # Solo se muestra para los miembros 1 y 3
        return self.round_number == 5 and self.participant.vars['order_number_Crisis'] in [1, 2]
    
    def vars_for_template(self):
        member3 = self.group.get_player_by_id(3)
        return {'member3_response': member3.crisis_group,
                'next_button_label': "Continuar"}
    
class CrisisWaitForMoneyDistribution3(WaitPage):
    def is_displayed(self):
        return self.round_number == 5
    
    def after_all_players_arrive(self):
        return  # Esto asegura que todos hayan pasado por DistributeMoneyPage antes de continuar
   
class ThankYouPage(Page):
    def is_displayed(self):
        return self.round_number == 5

    def vars_for_template(self):
        return dict(
            message="¡Gracias por participar en nuestro estudio!"
        )

page_sequence = [
    Controversial_Questions,
    Prueba_Question,
    Forming_Groups_WaitPage_Prueba,
    GroupingSyncWaitPage_Prueba,
    ShowContext_Prueba,
    PruebaQuestion1,
    PruebaWaitForMember1,
    PruebaShowResponseMember1,
    PruebaQuestionsForMember1,
    PruebaDistributeMoneyPage1,
    PruebaWaitForMoneyDistribution1,
    PruebaQuestion2,
    PruebaWaitForMember2,
    PruebaShowResponseMember2,
    PruebaQuestionsForMember2,
    PruebaDistributeMoneyPage2,
    PruebaWaitForMoneyDistribution2,
    PruebaQuestion3,
    PruebaWaitForMember3,
    PruebaShowResponseMember3,
    PruebaQuestionsForMember3,
    PruebaDistributeMoneyPage3,
    PruebaWaitForMoneyDistribution3,
    GlobalSyncWaitPage_Tabaco,
    Forming_Groups_WaitPage_Tabaco,
    GroupingSyncWaitPage_Tabaco,
    ShowContext_Tabaco,
    AntitabacoQuestion1,
    TabacoWaitForMember1,
    TabacoShowResponseMember1,
    TabacoQuestionsForMember1,
    TabacoDistributeMoneyPage1,
    TabacoWaitForMoneyDistribution1,
    AntitabacoQuestion2,
    TabacoWaitForMember2,
    TabacoShowResponseMember2,
    TabacoQuestionsForMember2,
    TabacoDistributeMoneyPage2,
    TabacoWaitForMoneyDistribution2,
    AntitabacoQuestion3,
    TabacoWaitForMember3,
    TabacoShowResponseMember3,
    TabacoQuestionsForMember3,
    TabacoDistributeMoneyPage3,
    TabacoWaitForMoneyDistribution3,
    GlobalSyncWaitPage_Arte,
    Forming_Groups_WaitPage_Arte,
    GroupingSyncWaitPage_Arte,
    ShowContext_Arte,
    ArteQuestion1,
    ArteWaitForMember1,
    ArteShowResponseMember1,
    ArteQuestionsForMember1,
    ArteDistributeMoneyPage1,
    ArteWaitForMoneyDistribution1,
    ArteQuestion2,
    ArteWaitForMember2,
    ArteShowResponseMember2,
    ArteQuestionsForMember2,
    ArteDistributeMoneyPage2,
    ArteWaitForMoneyDistribution2,
    ArteQuestion3,
    ArteWaitForMember3,
    ArteShowResponseMember3,
    ArteQuestionsForMember3,
    ArteDistributeMoneyPage3,
    ArteWaitForMoneyDistribution3,
    GlobalSyncWaitPage_Violencia,
    Forming_Groups_WaitPage_Violencia,
    GroupingSyncWaitPage_Violencia,
    ShowContext_Violencia,
    ViolenciaQuestion1,
    ViolenciaWaitForMember1,
    ViolenciaShowResponseMember1,
    ViolenciaQuestionsForMember1,
    ViolenciaDistributeMoneyPage1,
    ViolenciaWaitForMoneyDistribution1,
    ViolenciaQuestion2,
    ViolenciaWaitForMember2,
    ViolenciaShowResponseMember2,
    ViolenciaQuestionsForMember2,
    ViolenciaDistributeMoneyPage2,
    ViolenciaWaitForMoneyDistribution2,
    ViolenciaQuestion3,
    ViolenciaWaitForMember3,
    ViolenciaShowResponseMember3,
    ViolenciaQuestionsForMember3,
    ViolenciaDistributeMoneyPage3,
    ViolenciaWaitForMoneyDistribution3,
    GlobalSyncWaitPage_Crisis,
    Forming_Groups_WaitPage_Crisis,
    GroupingSyncWaitPage_Crisis,
    ShowContext_Crisis,
    CrisisQuestion1,
    CrisisWaitForMember1,
    CrisisShowResponseMember1,
    CrisisQuestionsForMember1,
    CrisisDistributeMoneyPage1,
    CrisisWaitForMoneyDistribution1,
    CrisisQuestion2,
    CrisisWaitForMember2,
    CrisisShowResponseMember2,
    CrisisQuestionsForMember2,
    CrisisDistributeMoneyPage2,
    CrisisWaitForMoneyDistribution2,
    CrisisQuestion3,
    CrisisWaitForMember3,
    CrisisShowResponseMember3,
    CrisisQuestionsForMember3,
    CrisisDistributeMoneyPage3,
    CrisisWaitForMoneyDistribution3,
    ThankYouPage
]