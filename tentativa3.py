# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt 
#biblioteca MQTT desenvolvida pela Fundação Eclipse

#paho.Client(client_id=””, clean_session=True, userdata=None, protocol=paho.MQTTv31)
#If you do not specify a client_id, a random id will be generated for you (and clean_session must be set to True). The userdata parameter can be any value or datatype that you wish and the data will be passed to all callbacks as the userdata variable

ipBroker = "iot.eclipse.org"
portBroker = 1883

#instrução de subscrição da mensagem dentro do calback on_connect. Isso é feito assim para que, uma vez que a conexão seja perdida, ao ser restabelecida a subscrição será novamente feita.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # O subscribe fica no on_connect pois, caso perca a conexão ele a renova
    # Lembrando que quando usado o #, você está falando que tudo que chegar após a barra do topico, será recebido

    client.subscribe("$SYS/#")
    
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


#definindo duas callbacks (funções que são chamadas quando ocorrem eventos do MQTT): 
client = mqtt.Client()
client.on_connect = on_connect #é chamada após a conexão
client.on_message = on_message # é chamada a cada mensagem que é recebida

# Conecta no MQTT Broker, no meu caso, o Mosquitto
client.connect(ipBroker,portBroker,60)


# Seta um usuário e senha para o Broker, se não tem, não use esta linha
#client.username_pw_set("USUARIO", password="SENHA")


# Inicia o loop
client.loop_forever()
