import os
import discord
from discord.ext import commands

from myserver import server_on

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot Online!")
    print("555")
    synced = await bot.tree.sync()
    print(f"{len(synced)} command(s)")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1298256171890901134)
    text = f"{member.mention} Are you new here!"
    await channel.send(text)

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1298256171890901134)
    text = f"{member.name} I hope you come back hehe"
    await channel.send(text)

TARGET_CHANNEL_ID = 1311277025708998687

class QuizModal(discord.ui.Modal, title="verification"):
    """ Modal ที่มี 3 คำถามในป๊อปอัปเดียว """
    
    answer1 = discord.ui.TextInput(label="1️⃣ สัตว์ที่ใหญ่ที่สุดในโลกคืออะไร?", placeholder="กรอกคำตอบที่นี่...", required=True)
    answer2 = discord.ui.TextInput(label="2️⃣ สีของท้องฟ้าเวลากลางวันคืออะไร?", placeholder="กรอกคำตอบที่นี่...", required=True)
    answer3 = discord.ui.TextInput(label="3️⃣ กรุงเทพฯ เป็นเมืองหลวงของประเทศอะไร?", placeholder="กรอกคำตอบที่นี่...", required=True)

    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id
        self.add_item(self.answer1)
        self.add_item(self.answer2)
        self.add_item(self.answer3)

    async def on_submit(self, interaction: discord.Interaction):
        """ เมื่อผู้ใช้ส่งคำตอบ ให้ส่งไปยังช่องที่กำหนด """
        channel = bot.get_channel(TARGET_CHANNEL_ID)

        if channel:
            answers_text = (
                f"📩 **คำตอบจาก {interaction.user.mention}:**\n"
                f"1️⃣ {self.answer1.value}\n"
                f"2️⃣ {self.answer2.value}\n"
                f"3️⃣ {self.answer3.value}"
            )
            await channel.send(answers_text)
            await interaction.response.send_message("เราจะตรวจสอบการยืนยันตัวตนของคุณ!", ephemeral=True)
        else:
            await interaction.response.send_message("error: 001", ephemeral=True)

class QuizSelect(discord.ui.View):
    @discord.ui.select(
        placeholder="",
        options=[
            discord.SelectOption(label="verification!", description=""),
        ]
    )
    async def select_callback(self, interaction: discord.Interaction, select: discord.ui.Select):
        if select.values[0] == "verification!":
            await interaction.response.send_modal(QuizModal(interaction.user.id))

@bot.command()
async def menu(ctx):
    """ ส่งเมนูตัวเลือก """
    view = QuizSelect()
    await ctx.send("📌 **เลือกเมนูเพื่อเริ่มทำแบบทดสอบ**", view=view)

server_on()

bot.run(os.getenv('TOKEN'))
