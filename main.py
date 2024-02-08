import discord
from discord.ext import commands
from discord import app_commands
from voice_generator import creat_WAV

intents = discord.Intents.default()
intents.message_content = True # メッセージの内容を取得する権限

client = commands.Bot(command_prefix='.', intents=intents)
voice_client = None


@client.event
async def on_ready():
    await client.tree.sync()
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.tree.command(name="join",description="ボイスチャンネルに入室し、読み上げを開始します。")
async def slash_join(interaction: discord.VoiceChannel):
    #voicechannelを取得
    vc = interaction.user.voice.channel
    #voicechannelに接続
    await vc.connect()

    await interaction.response.send_message("接続しました。")

@client.tree.command(name="bye",description="ボイスチャンネルに退出し、読み上げを終了します。")
async def slash_bye(interaction: discord.VoiceChannel):
    #切断
    await interaction.guild.voice_client.disconnect()

    await interaction.response.send_message("切断しました。")

@client.event
async def on_message(message):
    if message.guild.voice_client:
        print(message.content)
        creat_WAV(message.content)
        source = discord.FFmpegPCMAudio(executable="./ffmpeg/bin/ffmpeg.exe", source="output.wav")
        message.guild.voice_client.play(source)
    else:
        pass


client.run("your_discord_token")
