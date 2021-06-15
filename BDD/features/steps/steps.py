from typing import ContextManager
from behave import *
from twentyone import *


@given(u'a dealer')
def step_impl(context):
    context.dealer = Dealer()
    

@when(u'the round starts')
def step_impl(context):
    context.dealer.new_round()
    

@then(u'the dealer gives itself two cards')
def step_impl(context):
    assert (len(context.dealer.hand) == 2)


@then(u'the dealer chooses to play')
def step_impl(context):
    assert context.dealer.make_play() in ['stand','hit']


#----------------##----------------#
@given(u'a hand {total:d}')
def step_imp(context, total):
    context.dealer = Dealer()
    context.total = total

@when(u'the dealer determines a play')
def step_impl(context):
    context.dealer_play = context.dealer.determine_play(context.total)



#----------------##----------------#
@given(u'{hand}')
def step_impl(context, hand):
    context.dealer = Dealer()
    context.dealer.hand = hand.split(',')
    

@when(u'the dealer sums the card')
def step_impl(context):
    context.dealer_total = context.dealer.get_hand_total()
    

@then(u'the {total:d} is correct')
def step_impl(context, total):
    assert (context.dealer_total) == total



@then(u'the {play} is correct')
def step_impl(context, play):
    assert (context.dealer_play == play)