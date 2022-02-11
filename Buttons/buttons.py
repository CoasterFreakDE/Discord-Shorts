import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')


class StandardButton(discord.ui.Button):
    def __init__(self):
        super().__init__(
            label="Klicke mich!",
            style=discord.enums.ButtonStyle.blurple,
            custom_id="interaction:DefaultButton"
        )
    
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message("Yeyy! Du hast mich angeklickt.", ephemeral=True)
        
@bot.command()
async def hallo(ctx):
    view = discord.ui.View(timeout=None)
    view.add_item(StandardButton())
    await ctx.send(f"Hallo {ctx.author.mention}!", view=view)


bot.run("TOKEN-EINFÜGEN")