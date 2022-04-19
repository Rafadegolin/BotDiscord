import discord
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content == '$regras':
            await message.channel.send(f'Caro {message.author.name}, as regras do servidor são:{os.linesep}1. Não desrespeitas os membros (Somente eu posso insulta-los!){os.linesep}2. Tudo que é dito aqui, fica aqui!{os.linesep}3. Seja feliz!')
        elif message.content == "$ola":
            await message.channel.send(f'Oiii {message.author.name} seja muito mas muito bem vindo ao servido!!! Que seu dia seja incrível assim como você S2')

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            mensagem = f'{member.mention} acabou de entrar no {guild.name} seja bem vindo(a) :)'
            await guild.system_channel.send(mensagem)

intents = discord.Intents.default()
intents.members = True


client = MyClient(intents=intents)
client.run('OTY1OTY4NTYyNzM0OTAzMzY2.Yl66VA.ShfXgmDGULaEP1-0TqamTUUasi0')