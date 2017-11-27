
def parse_board(context):
    """
    Helper to extract the GoL board from the behave table representation of the cucumber steps.
    The board will be a NxN matrix stored as a list of lists in 'context.board'.
    """
    context.board = []
    context.board = [context.table.headings[:]]
    context.board.extend(r.cells for r in context.table.rows)

def print_board(context):
    for row in context.board:
        print(' '.join (row))


@given(u'the following setup')
def step_impl(context):
    parse_board(context)

@when(u'I evolve the board')
def step_impl(context):
    print("Board before evolve step:")
    print_board(context)
    print("TODO: implement evolution!")
    print("Board after evolve step: ")
    print_board(context)

@then(u'the center cell should be dead')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the center cell should be dead')

@then(u'the center cell should be alive')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the center cell should be alive')

@then(u'I should see the following board')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should see the following board')

