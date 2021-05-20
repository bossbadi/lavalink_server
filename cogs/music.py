from discord.ext import commands
import lavalink
from discord import utils
from discord import Embed

class MusicCog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.bot.music = lavalink.Client(bot.user.id)
    self.bot.music.add_node('https://bossbadi-hlavalink.herokuapp.com/', 80, 'youshallnotpass', 'us', 'default-node')  # Host, Port, Password, Region, Name
    self.bot.add_listener(self.bot.music.voice_update_handler, 'on_socket_response')
    self.bot.music.add_event_hook(self.track_hook)

  @commands.command(name='join')
  async def join(self, ctx):
    print('join command worked')
    print(ctx.author)
    member = ctx.author
    if member is not None and member.voice is not None:
      vc = member.voice.channel
      player = self.bot.music.player_manager.create(ctx.guild.id, endpoint=str(ctx.guild.region))
      if not player.is_connected:
        player.store('channel', ctx.channel.id)
        await self.connect_to(ctx.guild.id, str(vc.id))

  @commands.command(name='play')
  async def play(self, ctx, *, query):
    try:
      player = self.bot.music.player_manager.get(ctx.guild.id)
      query = f'ytsearch:{query}'
      results = await player.node.get_tracks(query)
      track = results['tracks'][0]

      player.add(requester=ctx.author.id, track=track)
      if not player.is_playing:
        await player.play()

    except Exception as error:
      print(error)
  
  async def track_hook(self, event):
    if isinstance(event, lavalink.events.QueueEndEvent):
      guild_id = int(event.player.guild_id)
      await self.connect_to(guild_id, None)
      
  async def connect_to(self, guild_id: int, channel_id: str):
    ws = self.bot._connection._get_websocket(guild_id)
    await ws.voice_state(str(guild_id), channel_id)

def setup(bot):
  bot.add_cog(MusicCog(bot))