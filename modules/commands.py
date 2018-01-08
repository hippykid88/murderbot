#!/usr/local/bin/python3.6
#pylint: disable = W, C
import discord
import asyncio
import random
from discord.ext import commands

class Commands():
    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=['murder'])
    async def Murder(self, ctx):
        """-The children whisper..."""
        await ctx.channel.send("Murder, Murder, Murder")

    @commands.command(aliases=['history'])
    async def History(self, ctx):
        """-When did this all start"""
        await ctx.channel.send("Murders Inc was founded in 1997")

    @commands.command(aliases=['chink'])
    async def Chink(self, ctx):
        """-Is this racist?"""
        await ctx.channel.send("The sound two swords make when they clash together - according to Jack")

    @commands.command(aliases=['joeling'])
    async def Joeling(self, ctx):
       """-yup its this"""
       await ctx.channel.send("Joeling is the act of masturbating while on vent")

    @commands.command(aliases=['oliver'])
    async def Oliver(self, ctx):
       """-I mean its Oliver"""
       await ctx.channel.send("RIP my dudes")

    @commands.command(aliases=['boat'])
    async def Boat(self, ctx):
       """-Am on a Boat!"""
       await ctx.channel.send('https://www.youtube.com/watch?v=avaSdC0QOUM')

    @commands.command(aliases=['godfather'])
    async def Godfather(self, ctx):
       """-The creator"""
       await ctx.channel.send('<@178193803033706496> you have been summoned')


    @commands.command(aliases=['ginger'])
    async def Ginger(self, ctx):
       """-Fuck these types of ppl"""
       await ctx.channel.send('Gingers are soulless bastards looking at you <@215484638108450817>')

    @commands.command(aliases=['sheriff'])
    async def Sheriff(self, ctx):
       """-Good times"""
       await ctx.channel.send('A good Sheriff always shoots his own deputy..twice for good measure')

    @commands.command(aliases=['will'])
    async def Will(self, ctx):
        """-The New guys in town"""
        await ctx.channel.send('Let me Know what I should put here young murderer')

    @commands.command(aliases=['dillon'])
    async def Dillon(self, ctx):
        """-Mr Silent"""
        await ctx.channel.send('one of the season members of Murderers Inc, quite but will fuck you up')

    @commands.command(aliases=['exile'])
    async def Exile(self, ctx):
        """-Can be a Dick for sure"""
        await ctx.channel.send('Drunkenly shouts on vent “GET TO THE FUCKING LUMBER MINES!”')

def setup(bot):
    bot.add_cog(Commands(bot))
