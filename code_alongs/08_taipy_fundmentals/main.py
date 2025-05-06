from taipy.gui import Gui
import taipy.gui.builder as tgb
import plotly.express as px

df = px.data.gapminder()
fig = px.line(df.query("country =='Sweden'"), x="year", y="pop")


selected_fruit = "avocado"
slider_value = 20

number1 = 3
number2 = 5

sum_ = number1 + number2
product = number1 * number2
quotient = number1 / number2
difference = number1 - number2

def perform_calculation(state):
    state.sum_ = int(state.number1) + int(state.number2)
    state.product = int(state.number1) * int(state.number2)
    state.difference = int(state.number1) - int(state.number2)
    state.quotient = int(state.number1) / int(state.number2)

def clear_results(state):
    state.sum_ = ""
    state.product = ""
    state.quotient = ""
    state.difference = ""

with tgb.Page() as page:
        with tgb.part(class_name="container card"):
            with tgb.layout(columns="1 1 1"):
                with tgb.part():
                    tgb.text("# Hello there taipy", mode = "md", class_name="color-primary")
                    tgb.text("Welcome to the world of reactive programming")
                
                  # binds to slider_value variable and makes it dynamic
                    tgb.slider(value="{slider_value}", min = 1, max = 50, step = 5,continuous=False)
                    tgb.text("Slider value is at {slider_value}")
                    tgb.text("Slider value is again at {slider_value}")

                    tgb.text("Select your favourite fruit")
                    tgb.selector(value="{selected_fruit}", lov=["tomato", "apple","avocado", "banana"], dropdown=True)
                    tgb.text("Yummy, {selected_fruit}")
                    tgb.image("assets/{selected_fruit}.jpg")

                with tgb.part() as column_calculator:
                    tgb.text("## Coolo Calculaturo", mode="md")
                    tgb.text("Typy in a number")
                    tgb.input("{number1}", on_change=clear_results)

                    tgb.text("Typy in another number")
                    # on change -> this function will run when value is changed
                    tgb.input("{number2}", on_change=clear_results)

                    tgb.text("You have typed in {number1} and {number2}")
                    #on action -> this function is runnded when clicked on button
                    tgb.button(label="Calculate", class_name="plain", on_action=perform_calculation)

                    tgb.text("{number1} + {number2} = {sum_}")

                with tgb.part() as column_data:
                    tgb.table("{df}")
                    tgb.chart(figure="{fig}")

if __name__ == "__main__":
    Gui(page).run(dark_mode=False, use_reloader=True, port=8080)