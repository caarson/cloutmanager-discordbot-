# Python 3.6 Discord.py, Emoji
# imports
import asyncio
import time
import emoji
import discord
from discord.ext import commands


########################################################################
# global methods / classes
########################################################################
class Utilities:
    def __init__(self):
        pass

    # deletes a channel given it's context
    async def delete_channel(self, ctx):
        await ctx.channel.delete()

    # renames a channel given its context
    async def rename_channel(self, ctx):
        def check(m):
            return m.author.id == ctx.author.id and m.channel == ctx.channel

        await ctx.send("**Please enter a new channel name**\n ")
        try:
            new_name = await bot.wait_for('message', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send('Request Timed Out')
            return
        try:
            await ctx.channel.edit(name=new_name.content)
            return True
        except Exception as E:
            print(E)
            return False


class Ticketing:  # ticketing utilties
    def __init__(self):
        # declare ticket count:
        try:
            self.ticket_count = int(input("number of tickets already created: "))
        except:
            print("[!] enter an integer whole value!")
            self.ticket_count = int(input("number of tickets already created: "))

    # adds to ticket count then returns self.ticket_count
    def add_to_ticket_count(self):
        self.ticket_count = self.ticket_count + 1
        return self.ticket_count

    # renames a ticket's suffix given it's context
    async def rename_ticket(self, ctx, suffix):
        channel_name = ctx.channel.name
        channel_name = channel_name.split('-', -1)[0]
        suffix = "-" + suffix
        channel_name = channel_name + suffix
        await ctx.channel.edit(name=channel_name)
        print("renamed a channel to: " + channel_name)


# declare class instances:
Utilities = Utilities()
Ticketing = Ticketing()

########################################################################
# variables
########################################################################
token = "NjA3NzE1OTA5NTMxODYwOTky.XjhIRw.v_ioVRinP7l1u6Y34StC56QvRDI"  # Get at discordapp.com/developers/applications/me | switch to change server location.
bot = commands.Bot(command_prefix='>')
method_message = "a method has been executed."
payment_email = 'derejrcar@gmail.com'
ticket_count = Ticketing.ticket_count
bot_name = "cloutmanager"
backend_channel_number = 610121718484303875


########################################################################
# bot events
########################################################################
@bot.event
async def on_ready():  # deploys the clout manager
    print(bot_name + ' has been deployed.')
    backend = bot.get_channel(backend_channel_number)  # get backend channel.
    await backend.send(bot_name + ' has been deployed.')


@bot.event
async def on_member_join(member):
    print(str(member) + ' has joined the server')


@bot.event
async def on_message(message):
    if message.guild:
        role = message.guild.get_role(609545936972152832)  # get role attribute
        if role.mention in message.content:  # if role is inside of the message.content, perform actions.

            guild = message.guild  # get guild (server)
            member = message.author  # get the author of the message
            sales_role = message.guild.get_role(609545936972152832)  # get sales role

            # overwrite options - permissions
            overwrites = {
                guild.default_role: discord.PermissionOverwrite(read_messages=False),
                member: discord.PermissionOverwrite(read_messages=True, read_message_history=True),
                guild.me: discord.PermissionOverwrite(read_messages=True),
                sales_role: discord.PermissionOverwrite(read_messages=True)
            }

            category = bot.get_channel(610107824869212211)  # get category
            channel = await category.create_text_channel(name="ticket" + str(Ticketing.add_to_ticket_count()),
                                                         overwrites=overwrites)  # create channel
            print("created channel: " + str(channel))  # print channel to console.
    await bot.process_commands(message)


########################################################################
# bot commands
########################################################################
@bot.command()
async def issue(ctx):  # confirms the payment then executes rename_channel.
    await ctx.send(emoji.emojize('@here :: There is an issue regarding the order.\n \n :warning:'))

    suffix = "issuewithorder"

    await Ticketing.rename_ticket(ctx, suffix)


@bot.command()
async def list_options(ctx):  # confirms the payment then executes rename_channel.
    await ctx.send(emoji.emojize('@here :: Clout Services offers a variety of services!\n \n #standard #premium #exclusive '))


@bot.command()
async def exclusive(ctx):  # confirms the payment then executes rename_channel.
    await ctx.send(emoji.emojize('@here :: Printing exclusive script...'))

    file = open("exclusive.txt", "r").read()

    await ctx.send(emoji.emojize(file))

    suffix = "exclusive"

    await Ticketing.rename_ticket(ctx, suffix)


@bot.command()
async def premium(ctx):  # confirms the payment then executes rename_channel.
    await ctx.send(emoji.emojize('@here :: Printing premium script...'))

    file = open("premium.txt", "r").read()

    await ctx.send(emoji.emojize(file))

    suffix = "premium"

    await Ticketing.rename_ticket(ctx, suffix)


@bot.command()
async def preview(ctx):  # confirms the payment then executes rename_channel.
    await ctx.send(emoji.emojize('@here :: A preview is being generated...'))

@bot.command()
async def standard(ctx):  # confirms the payment then executes rename_channel.
    await ctx.send(emoji.emojize('@here :: Printing standard script...'))

    file = open("standard.txt", "r").read()

    await ctx.send(emoji.emojize(file))

    suffix = "standard"

    await Ticketing.rename_ticket(ctx, suffix)

@bot.command()
async def delete_channel(ctx):  # prints delete channel then runs delete from utilities
    await ctx.send(emoji.emojize('Deleting channel...'))

    time.sleep(1)

    await Utilities.delete_channel(ctx)

@bot.command()
async def confirm(ctx):  # confirms the payment then executes rename_ticket.
    await ctx.send(emoji.emojize('Confirmed payment.\n \n :white_check_mark:'))

    suffix = "paymentconfirmed"

    await Ticketing.rename_ticket(ctx, suffix)


@bot.command()
async def awaiting_payment(ctx):  # marks ticket as awaiting payment
    await ctx.send(emoji.emojize('@here :: Please send full amount to ' + payment_email + '.\n \n :white_check_mark:'))

    suffix = "awaitingpayment"

    await Ticketing.rename_ticket(ctx, suffix)


@bot.command()
async def inactive(ctx):  # renames ticket to no-response message
    await ctx.send(emoji.emojize('Marked as no-response.\n \n :white_check_mark:'))

    suffix = "nobotresponse"

    await Ticketing.rename_ticket(ctx, suffix)


@bot.command()
async def start(ctx):  # starts a project
    await ctx.send(emoji.emojize('Project marked as in-progress.\n \n :white_check_mark:'))

    suffix = "inprogress"

    await Ticketing.rename_ticket(ctx, suffix)


@bot.command()
async def complete(ctx):
    await ctx.send(emoji.emojize('Project marked as completed.\n \n :white_check_mark:'))

    suffix = "projectcompleted"

    await Ticketing.rename_ticket(ctx, suffix)


bot_ran = False
while not bot_ran:
    try:
        bot.run(token)
        bot_ran = True
    except:
        print('trying run bot again...')
        try:
            time.sleep(1000)
            bot.run(token)
            bot_ran = True
        except:
            print("failed to run bot again!")
            bot_ran = False

