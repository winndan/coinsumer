from fasthtml.common import *
from monsterui.all import *

def home():
    return Html(
    Head(
        Meta(charset='UTF-8'),
        Meta(name='viewport', content='width=device-width, initial-scale=1.0'),
        Link(href='https://cdn.jsdelivr.net/npm/remixicon@4.3.0/fonts/remixicon.css', rel='stylesheet'),
        Link(rel='stylesheet', href='static/styles.css'),
        Title('Coinsumer - AI-Powered Crypto Analysis & Trading')
    ),
    Body(
        Header(
            Nav(
                Div(
                    Div(
                        A(
                            Img(src='static/Coinsumerx-removebg.png', alt='Coinsumer Logo', cls='logo-img'),
                            href='#',
                            cls='logo'
                        ),
                        cls='nav__logo'
                    ),
                    Div(
                        I(cls='ri-menu-line'),
                        id='menu-btn',
                        cls='nav__menu__btn'
                    ),
                    cls='nav__header'
                ),
                Ul(
                    Li(
                        A('Home', href='#home')
                    ),
                    Li(
                        A('Story', href='#story')
                    ),
                    Li(
                        A('AI Products', href='#product')
                    ),
                    Li(
                        A('Data Market', href='#news')
                    ),
                    Li(
                        Button('Login', cls='btn')
                    ),
                    id='nav-links',
                    cls='nav__links'
                )
            ),
            Div(
                H1('AI agents for Crypto Market'),
                P('Analyze, react, and optimize crypto trading with advanced AI-powered insights. Stay ahead of the market with real-time data and AI-driven strategies.'),
                Div(
                    Button(
                        'Sign Up for Free',
                        Span(
                            I(cls='ri-arrow-right-up-line')
                        ),
                        cls='btn'
                    ),
                    Button(
                        'Explore Agents',
                        Span(
                            I(cls='ri-play-circle-fill')
                        ),
                        cls='btn'
                    ),
                    cls='header__btns'
                ),
                cls='header__content'
            ),
            Div(
                Img(src='static/headerx.jpg', alt='header'),
                cls='header__image'
            ),
            id='home'
        ),
        Section(
            Div(
                H3('OUR FEATURES', cls='section__subheader'),
                H2('AI-Powered Crypto Assistant & Market Analysis', cls='section__header'),
                P('Equip yourself with cutting-edge AI technology to analyze trends, react market movements, and enhance your crypto trading strategies.'),
                Div(
                    Button(
                        'Explore agent',
                        Span(
                            I(cls='ri-arrow-right-up-line')
                        ),
                        cls='btn'
                    ),
                    cls='feature__btn'
                ),
                cls='feature__content'
            ),
            Div(
                Div(
                    Span(
                        I(cls='ri-bar-chart-line')
                    ),
                    H4('Data-Driven Market Insights'),
                    P('Leverage AI to understand patterns and make informed market decisions.'),
                    cls='feature__card'
                ),
                Div(
                    Span(
                        I(cls='ri-database-2-line')
                    ),
                    H4('Comprehensive Data Aggregation'),
                    P('Combines historical data, real-time updates, sentiment and AI-driven analytics.'),
                    cls='feature__card'
                ),
                Div(
                    Span(
                        I(cls='ri-cloud-line')
                    ),
                    H4('Seamless Exchange Integration'),
                    P('Connect to major crypto exchanges, news feeds, and blockchain data providers.'),
                    cls='feature__card upcoming-feature'
                ),
                Div(
                    Span(
                        I(cls='ri-cpu-line')
                    ),
                    H4('AI-Powered Strategy Execution'),
                    P('Automate trades with AI-driven strategies optimized for market conditions. (Available Soon)'),
                    cls='feature__card upcoming-feature'
                ),
                cls='feature__grid'
            ),
            id='story',
            cls='section__container feature__container'
        ),
        Section(
            Div(
                Img(src='static/banner-1.jpg', alt='banner'),
                H4('AI-Powered Market Analysis'),
                Button(
                    'Learn More',
                    Span(
                        I(cls='ri-arrow-right-up-line')
                    ),
                    cls='btn'
                ),
                cls='banner__card'
            ),
            Div(
                Img(src='static/banner-2.jpg', alt='banner'),
                H4('Data-Driven Decision Making'),
                Button(
                    'Learn More',
                    Span(
                        I(cls='ri-arrow-right-up-line')
                    ),
                    cls='btn'
                ),
                cls='banner__card'
            ),
            cls='section__container banner__container'
        ),
        Section(
            Div(
                Div(
                    Div(
                        Div(
                            Span(
                                I(cls='ri-line-chart-line')
                            ),
                            H4('Real-Time AI Insights')
                        ),
                        P('Stay ahead with continuous AI-driven market monitoring and instant alerts.'),
                        cls='specs__card'
                    ),
                    cls='specs__row'
                ),
                Div(
                    Div(
                        Div(
                            Span(
                                I(cls='ri-database-2-line')
                            ),
                            H4('Data Feed Hub')
                        ),
                        P('Access differenct types of crypto market data to power AI agent.'),
                        cls='specs__card'
                    ),
                    cls='specs__row'
                ),
                cls='section__container specs__container'
            ),
            cls='specs'
        ),
        Section(
            H3('OUR PRODUCTS', cls='section__subheader'),
            H2('Empower your strategy with AI-driven market analysis.', cls='section__header'),
            Div(
                Ul(
                    Li(
                        P('AI Agents Market Analyzer')
                    ),
                    Li(
                        P('Crypto Data Market')
                    ),
                    Li(
                        P('Customizable AI Strategies', cls='upcoming-feature')
                    ),
                    cls='product__list'
                ),
                Div(
                    Img(src='static/product.jpg', alt='product'),
                    P('Revolutionizing crypto market analysis with AI-powered insights\r\n             and automation.'),
                    Div(
                        Button(
                            'Explore Products',
                            Span(
                                I(cls='ri-arrow-right-up-line')
                            ),
                            cls='btn'
                        ),
                        cls='product__btn'
                    ),
                    cls='product__content'
                ),
                cls='product__grid'
            ),
            id='product',
            cls='section__container product__container'
        ),
        Footer(
            Div(
                Div(
                    Div(
                        A(
                             Img(src='static/Coinsumerx-removebg.png', alt='Coinsumer Logo', cls='logo-img'),
                            href='#',
                            cls='logo'
                        ),
                        cls='footer__logo'
                    ),
                    Ul(
                        Li(
                            A(
                                Span(
                                    I(cls='ri-mail-line')
                                ),
                                'Email: llanesdanmarc@gmail.com',
                                href='mailto:llanesdanmarc@gmail.com',
                                cls='contact-link'
                            )
                        ),
                        Li(
                            A(
                                Span(
                                    I(cls='ri-map-pin-line')
                                ),
                                'South Cembo, Taguig City',
                                href='#'
                            )
                        ),
                        Li(
                            A(
                                Span(
                                    I(cls='ri-facebook-line')
                                ),
                                'Facebook',
                                href='https://facebook.com/coinsumer',
                                target='_blank'
                            )
                        ),
                         Li(
                            A(
                                Span(
                                    I(cls='ri-instagram-line')
                                ),
                                'Instagram',
                                href='https://instagram.com/coinsumer',
                                target='_blank'
                            )
                        ),
                        cls='footer__links'
                    ),
                    cls='footer__col'
                ),
                Div(
                    H4('Menu'),
                    Ul(
                                    Li(A(
                    Span(I(cls='ri-home-line')),
                    'Home', href='#home', cls='nav-link'
                )),
                Li(A(
                    Span(I(cls='ri-information-line')),
                    'About', href='#about', cls='nav-link'
                )),
                Li(A(
                    Span(I(cls='ri-robot-line')),
                    'AI Agents', href='#ai-agents', cls='nav-link'
                )),
                Li(A(
                    Span(I(cls='ri-database-line')),
                    'Data Feeds', href='#data-feeds', cls='nav-link'
                )),
                     
                        cls='footer__links'
                    ),
                    cls='footer__col'
                ),
                Div(
                    H2('Join our newsletter'),
                    P('Stay tuned for new product updates'),
                    Form(
                        Input(type='text', placeholder='Your email here'),
                        Button('Subscribe', cls='btn'),
                        action='/'
                    ),
                    cls='footer__col'
                ),
                cls='section__container footer__container'
            ),
            Div('Copyright © 2025 Coinsumer technologies. All rights reserved.', cls='footer__bar'),
            id='news',
            cls='footer'
        ),
        Script(src='https://unpkg.com/scrollreveal'),
        Script(src='static/main.js')
    ),
    lang='en'
)