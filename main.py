# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import dash
import dash_html_components as html
import dash_daq as daq
import plotly.offline as pyo
import plotly.graph_objs as go
import dash_core_components as dcc
import webbrowser
from dash.dependencies import Input , Output ,State
import base64
#import serial
import requests
import os
import time
import dash_bootstrap_components as dbc


app = dash.Dash(__name__,
                meta_tags=[{'name': 'viewport',
                           'content': 'width=device-width, initial-scale=1.0, maximum-scale=3.2, minimum-scale=0.5,'}])

page1_header = html.H1(children='Showroom',
                       style=dict(color='white', fontWeight='bold',fontSize=28))

lighting_menu = dcc.Dropdown(
    id='dropdown',
    options=[
        dict(label='Concept', value='a1'),
        dict(label='Meeting Room', value='a2'),
        dict(label='Back End', value='a3'),
        dict(label='Reality', value='a4'),
        dict(label='Stand Alone', value='a5'),
        dict(label='Low Current', value='a6'),
        dict(label='Reception', value='a7'),
        dict(label='Show Box', value='a8')
    ],
    value='a1'
    , style=dict(color='#42A5F5', fontWeight='bold',fontColor='white', border='2px solid #42A5F5 '))


lighting_menu_div = html.Div([lighting_menu], style=dict(color='#42A5F5'))

encoded = base64.b64encode(open('2a-logo.png', 'rb').read())
logo_image = html.Img(src='data:image/png;base64,{}'.format(encoded.decode()), id='img2', height=100, width=150)
logo_image_div = html.Div(logo_image,
                          style=dict(backgroundColor='white'))

page1_header_div = html.Div([page1_header], style=dict(textAlign='center'))

Aw_button1 = dbc.Button("On/Off",id='my-indicator-button1',color='primary',size="lg",
                        style=dict(marginLeft='0%',paddingLeft='10%',paddingRight='10%'))

Aw_button1_div = html.Div(Aw_button1, style=dict(display='inline-block', border='3px solid black',width='25%'))

Aw_button2 = dbc.Button("On/Off",id='my-indicator-button2',color='primary',size="lg",
                        style=dict(marginLeft='0%',paddingLeft='10%',paddingRight='10%'))

Aw_button2_div = html.Div(Aw_button2, style=dict(display='inline-block', border='3px solid black',width='25%'))

Aw_button3 = dbc.Button("On/Off",id='my-indicator-button3',color='primary',size="lg",
                        style=dict(marginLeft='0%',paddingLeft='10%',paddingRight='10%'))

Aw_button3_div = html.Div(Aw_button3, style=dict(display='inline-block', border='3px solid black',width='25%'))

Aw_button4 = dbc.Button("On/Off",id='my-indicator-button4',color='primary',size="lg",
                        style=dict(marginLeft='0%',paddingLeft='10%',paddingRight='10%'))

Aw_button4_div = html.Div(Aw_button4, style=dict(display='inline-block', border='3px solid black',width='25%'))

Aw_button5 = dbc.Button("On/Off",id='my-indicator-button5',color='primary',size="md",
                        style=dict(marginLeft='0%',paddingLeft='10%',paddingRight='10%', display='inline-block'))
ac1_text= html.Div("AC-1",style=dict(fontWeight='bold',color='white',marginLeft='10%', display='inline-block'))

ac1_plus_button=dbc.Button("+",id='ac1_plus',color='primary',size="sm",
                        style=dict(marginLeft='0%',paddingLeft='10%',paddingRight='10%',fontWeight='bold',fontSize=22,display='inline-block'))

ac1_minus_button=dbc.Button("-",id='ac1_minus',color='primary',size="sm",
                        style=dict(marginLeft='10%',paddingLeft='10%',paddingRight='10%',fontWeight='bold',fontSize=22,display='inline-block'))

Aw_header = html.H1(children='Lighting - Alex Wall', id='aw_header',style=dict(color='white',
                                    fontWeight='bold' , fontSize=22))





Ma_button1 = html.Button('On/Off', id='Ma-button1', n_clicks=0
                         , style=dict( fontSize=20)

                         )
Ma_button1_div = html.Div(Ma_button1, style=dict(display='inline-block',
                                                 border='3px solid black'))
Ma_button2 = html.Button('On/Off', id='Ma-button2', n_clicks=0
                         , style=dict( fontSize=20)
                         )
Ma_button2_div = html.Div(Ma_button2, style=dict(display='inline-block',
                                                 border='3px solid black'))
Ma_button3 = html.Button('On/Off', id='Ma-button3', n_clicks=0
                         , style=dict( fontSize=20)

                         )
Ma_button3_div = html.Div(Ma_button3, style=dict(display='inline-block',
                                                 border='3px solid black'))
Ma_button4 = html.Button('On/Off', id='Ma-button4', n_clicks=0
                         , style=dict( fontSize=20)

                         )
Ma_button4_div = html.Div(Ma_button4, style=dict(display='inline-block',
                                                 border='3px solid black'))

Ma_button5 = html.Button('On/Off', id='Ma-button5', n_clicks=0
                         , style=dict( fontSize=20)

                         )
Ma_button5_div = html.Div(Ma_button5, style=dict(display='inline-block',
                                                 border='3px solid black'))

Ma_button6 = html.Button('On/Off', id='Ma-button6', n_clicks=0
                         , style=dict( fontSize=20)

                         )
Ma_button6_div = html.Div(Ma_button6, style=dict(display='inline-block',
                                                 border='3px solid black'))


color_picker = daq.ColorPicker(
    label=dict(label='Color Picker', style=dict(color='white')),
    value=dict(rgb=dict(r=155, g=213, b=123, a=0)), id='cp', size=170
)
color_picker_div = html.Div(color_picker, style=dict())

rgb_text = html.H1(id='rgb-text', children='Automate your life',
                   style=dict(color='skyblue', fontWeight='bold',fontSize=20))

rgb_text_div = html.Div(rgb_text, style=dict(textAlign='center'))


image_file = 'sharp1.png'
encoded = base64.b64encode(open(image_file, 'rb').read())
ac_image = html.Img(src='data:image/png;base64,{}'.format(encoded.decode()), id='img1', height=75, width=140)
ac_image_div = html.Div(ac_image, style=dict())

encoded = base64.b64encode(open(image_file, 'rb').read())
ac2_image = html.Img(src='data:image/png;base64,{}'.format(encoded.decode()), id='img3', height=100, width=220)
ac2_image_div = html.Div(ac2_image, style=dict())


encoded = base64.b64encode(open('off22.jpg', 'rb').read())
bulb1_off = html.Img(src='data:image/png;base64,{}'.format(encoded.decode()), id='bulb1_off', height=100, width=70)
encoded = base64.b64encode(open('off22.jpg', 'rb').read())
bulb2_off = html.Img(src='data:image/png;base64,{}'.format(encoded.decode()), id='bulb2_off', height=100, width=70)
encoded = base64.b64encode(open('off22.jpg', 'rb').read())
bulb3_off = html.Img(src='data:image/png;base64,{}'.format(encoded.decode()), id='bulb3_off', height=100, width=70)
encoded = base64.b64encode(open('off22.jpg', 'rb').read())
bulb4_off = html.Img(src='data:image/png;base64,{}'.format(encoded.decode()), id='bulb4_off', height=100, width=70)


encoded = base64.b64encode(open('on22.jpg', 'rb').read())
bulb1_on = html.Img(src='data:image/png;base64,{}'.format(encoded.decode()), id='bulb1_on', height=100, width=70)
encoded = base64.b64encode(open('on22.jpg', 'rb').read())
bulb2_on = html.Img(src='data:image/png;base64,{}'.format(encoded.decode()), id='bulb2_on', height=100, width=70)
encoded = base64.b64encode(open('on22.jpg', 'rb').read())
bulb3_on = html.Img(src='data:image/png;base64,{}'.format(encoded.decode()), id='bulb3_on', height=100, width=70)
encoded = base64.b64encode(open('on22.jpg', 'rb').read())
bulb4_on = html.Img(src='data:image/png;base64,{}'.format(encoded.decode()), id='bulb4_on', height=100, width=70)

bulb1_div = html.Div(bulb1_off,id='bulb_div1', style=dict(paddingLeft='0%'))
bulb2_div = html.Div(bulb2_off,id='bulb_div2', style=dict(marginLeft='0%'))
bulb3_div = html.Div(bulb3_off,id='bulb_div3', style=dict(marginLeft='0%'))
bulb4_div = html.Div(bulb4_off,id='bulb_div4', style=dict(marginLeft='0%'))

acs_power1 = daq.Indicator(
    id='Acs_power1',
    label=dict(label="Ac1 Off", style=dict(fontSize=20, color='white')),
    labelPosition="bottom",
    value=True,
    color='red',
    size=20
)
acs_power1_div = html.Div(acs_power1, style=dict())

acs_power2 = daq.Indicator(
    id='Acs_power2',
    label=dict(label="Ac2 Off", style=dict(fontSize=20, color='white')),
    labelPosition="bottom",
    value=True,
    color='red',
    size=20
)
acs_power2_div = html.Div(acs_power2, style=dict())

Acs_header = html.H1(children='Air Conditioners Control',
                     style=dict(color='white',  fontWeight='bold'
                                , fontSize=22))

Ac1_button = html.Button('On/Off', id='ac1-button', n_clicks=0
                         , style=dict( fontSize=20)
                         )
Ac1_button_div = html.Div(Ac1_button, style=dict(  border='3px solid black'))

Ac2_button = html.Button('On/Off', id='ac2-button', n_clicks=0
                         , style=dict( fontSize=20)

                         )
Ac2_button_div = html.Div(Ac2_button, style=dict( border='3px solid black'))

acs_div = html.Div([ac_image_div, Ac1_button_div, acs_power1_div, ac2_image_div, Ac2_button_div, acs_power2_div],
                   style=dict(  border='1px solid black', backgroundColor='rgb(60, 60, 60)'))

room_temp = daq.Thermometer(
    min=0, color="#E65100",
    max=100,
    value=21,
    showCurrentValue=True,height=100,width=15,
    units="C", label=dict(label='Room Temp(℃)', style=dict(color='white', fontSize=14)) ,id='room-temp'
)

room_temp_div = html.Div(room_temp, style=dict(display='inline-block'))

server_temp = daq.Thermometer(
    min=0, color="#E65100",
    max=100,
    value=60,
    showCurrentValue=True,height=100,width=15,
    units="C", label=dict(label='Server Temp(℃)', style=dict(color='white', fontSize=14)) , id='server-temp'
)

server_temp_div = html.Div(server_temp, style=dict(display='inline-block'))

temp_header = html.H1(children='Temperature Monitoring',
                      style=dict(color='white', fontWeight='bold'
                                 , fontSize=22))
temp_div = html.Div([room_temp_div, server_temp_div],
                    style=dict( border='1px solid black', backgroundColor='rgb(60, 60, 60)'))

interval=dcc.Interval(id="timing",interval=1000,n_intervals=0)

bulb1_text=html.Div("Conc. S1",style=dict(textAlign='Center',fontWeight='bold',color='white'))
bulb2_text=html.Div("Conc. S2",style=dict(textAlign='Center',fontWeight='bold',color='white'))
bulb3_text=html.Div("Conc. S3",style=dict(textAlign='Center',fontWeight='bold',color='white'))
bulb4_text=html.Div("Conc. S4",style=dict(textAlign='Center',fontWeight='bold',color='white'))
app.layout = html.Div([   dbc.Row( [ dbc.Col([ page1_header_div] ),

                      dbc.Row([     dbc.Col([ lighting_menu,html.Br()] ,xl=dict(size=3,offset=1),lg=dict(size=3,offset=1),
                     md=dict(size=4,offset=1),sm=dict(size=10,offset=1),xs=dict(size=10,offset=1))
                                               ]) ,

 dbc.Row([dbc.Col(   [ dbc.Card( dbc.CardBody( [  Aw_button1 ,html.Br(),html.Br(), bulb1_div,bulb1_text ])
                              , style=dict())   ],xl=dict(size=2,offset=1),lg=dict(size=2,offset=1),
                     md=dict(size=3,offset=1),sm=dict(size=5,offset=1),xs=dict(size=5,offset=1)
                                     ) ,
         dbc.Col([ dbc.Card( dbc.CardBody( [  Aw_button2 ,html.Br(),html.Br(), bulb2_div,bulb2_text ])
                              , style=dict()) ,html.Br()   ],xl=dict(size=2,offset=1),lg=dict(size=2,offset=1),
                     md=dict(size=3,offset=1),sm=dict(size=5,offset=1),xs=dict(size=5,offset=1)
                                     ),
          dbc.Col([dbc.Card(dbc.CardBody([Aw_button3, html.Br(), html.Br(), bulb3_div, bulb3_text])
                            , style=dict())], xl=dict(size=2, offset=1), lg=dict(size=2, offset=1),
                  md=dict(size=3, offset=1), sm=dict(size=5, offset=1), xs=dict(size=5, offset=1)
                  ) ,
          dbc.Col([dbc.Card(dbc.CardBody([Aw_button4, html.Br(), html.Br(), bulb4_div, bulb4_text])
                            , style=dict()),html.Br()], xl=dict(size=2, offset=1), lg=dict(size=2, offset=1),
                  md=dict(size=3, offset=1), sm=dict(size=5, offset=1), xs=dict(size=5, offset=1)
                  ) ,

          dbc.Col([dbc.Card(dbc.CardBody([room_temp])
                            , style=dict(height='235px'))], xl=dict(size=2, offset=1), lg=dict(size=2, offset=1),
                  md=dict(size=3, offset=1), sm=dict(size=5, offset=1), xs=dict(size=5, offset=1)
                  ) ,

          dbc.Col([dbc.Card(dbc.CardBody([server_temp])
                            , style=dict(height='235px')),html.Br()], xl=dict(size=2, offset=1), lg=dict(size=2, offset=1),
                  md=dict(size=3, offset=1), sm=dict(size=5, offset=1), xs=dict(size=5, offset=1)
                  ) ,

          dbc.Col([dbc.Card([ dbc.CardBody([Aw_button5,ac1_text,html.Br(),html.Br(),ac_image,html.Br(),html.Br(),ac1_plus_button,ac1_minus_button]) ]
                            , style=dict(height='235px'))], xl=dict(size=2, offset=1), lg=dict(size=3, offset=1),
                  md=dict(size=3, offset=1), sm=dict(size=8, offset=2), xs=dict(size=8, offset=2)
                  )

          ] ,no_gutters=False )
#dbc.CardImg(src="app.get_asset_url('sharp1.png')", top=True),




  ]
)









] )
#scmd = "/usr/bin/chromium-browser --start-fullscreen www.google.de"
#os.system('--remote-debugging-port=9222 --user-data-dir="D:\sel_debug"')
#webbrowser.open('https://user:2a@192.168.1.230')
#webbrowser.open('http://127.0.0.1:8555/')

try:
    x=requests.get('https://user:12345678@192.168.1.230',verify=False)
    print(x)


except requests.exceptions.RequestException as error:
    print("Error: ", error)







start_up=1
server_temp=30
@app.callback(
    Output('bulb_div1', 'children') ,
    [Input('my-indicator-button1', 'n_clicks')]
)

def bulb1_state(clicks):

    if clicks % 2 == 0:

        return bulb1_off

    else:

        return bulb1_on

@app.callback(
    Output('bulb_div2', 'children') ,
    [Input('my-indicator-button2', 'n_clicks')]
)

def bulb2_state(clicks):

    if clicks % 2 == 0:

        return bulb2_off

    else:

        return bulb2_on

@app.callback(
    Output('bulb_div3', 'children') ,
    [Input('my-indicator-button3', 'n_clicks')]
)

def bulb3_state(clicks):

    if clicks % 2 == 0:

        return bulb3_off

    else:

        return bulb3_on

@app.callback(
    Output('bulb_div4', 'children') ,
    [Input('my-indicator-button4', 'n_clicks')]
)

def bulb4_state(clicks):

    if clicks % 2 == 0:

        return bulb4_off

    else:

        return bulb4_on


@app.callback(
    Output('server-temp', 'value') ,
    [Input('timing', 'n_intervals')]
)
def update_temp(n_intervals):
    global server_temp
    if server_temp<60:
        server_temp+=2
    else :
        server_temp-=2
    return server_temp

@app.callback(
    Output('rgb-text', 'style'),
    [Input('cp', 'value')]
)
def led_strip(led_color):
    r = led_color['rgb']['r']
    g = led_color['rgb']['g']
    b = led_color['rgb']['b']
    return dict(color='rgb({},{},{})'.format(r, g, b), fontWeight='bold',fontSize=20)






@app.callback(
    [Output('Aw1_state', 'color'), Output('Aw1_state', 'label')],
    [Input('my-indicator-button1', 'n_clicks')])
def update_aw_s1(button_clicks):
    global start_up
    if start_up==1:
        start_up=0

    if( button_clicks % 2) == 0:
        color = 'white'
        #requests.get("https://user:12345678@192.168.1.230/json.htm?type=command&param=switchlight&idx=50&switchcmd=Off"
         #            , verify=False)
        mylabel = dict(label="S1 Off", style=dict(fontSize=20, color='white'))

    else:
        color='yellow'
       # requests.get("https://user:12345678@192.168.1.230/json.htm?type=command&param=switchlight&idx=50&switchcmd=On"
         #            , verify=False)
        mylabel = dict(label="S1 On", style=dict(fontSize=20, color='white'))

    return (color, mylabel)


last_state=0




@app.callback(
    [Output('Acs_power1', 'color'), Output('Acs_power1', 'label')],
    [Input('ac1-button', 'n_clicks')])
def update_ac1(button_clicks):
    color = 'red'

    if button_clicks % 2 == 0:
        color = 'red'
        mylabel = dict(label="Ac1 Off", style=dict(fontSize=16, color='white'))

    else:
        color = 'green'
        mylabel = dict(label="Ac1 On", style=dict(fontSize=16, color='white'))

    return (color, mylabel)


@app.callback(
    [Output('Acs_power2', 'color'), Output('Acs_power2', 'label')],
    [Input('ac2-button', 'n_clicks')])
def update_ac2(button_clicks):
    color = 'red'

    if button_clicks % 2 == 0:
        color = 'red'
        mylabel = dict(label="Ac2 Off", style=dict(fontSize=16, color='white'))

    else:
        color = 'green'
        mylabel = dict(label="Ac2 On", style=dict(fontSize=16, color='white'))

    return (color, mylabel)


#@app.callback(
  #  [Output('bulb_div1', 'children')],
 #   [Input('dropdown', 'value')]
#)
#def update_aw(menu):




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run_server(debug=False,port=8050)

