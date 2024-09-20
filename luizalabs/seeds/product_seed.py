from sqlalchemy import select
from sqlalchemy.orm import Session

from luizalabs.database.db_connection import engine
from luizalabs.models.product import Product


def check_if_products_exist(session: Session) -> Product:
    result = session.execute(select(Product).limit(1))
    return result.scalar()


# Função para inserir produtos
def seed_products():
    with Session(engine) as session:
        products_in_database = check_if_products_exist(session)

        if not products_in_database:
            products = [
                Product(
                    title='Smart TV 70” 4K UHD LED Samsung '
                    'Crystal 70DU8000 - Wi-Fi Bluetooth '
                    'Alexa 3 HDMI',
                    price=4799,
                    image=(
                        'https://a-static.mlcdn.com.br/800x560/smart-tv-70-4k-uhd-led-samsung-'
                        'crystal-70du8000-wi-fi-bluetooth-alexa-3-hdmi/magazineluiza/238244800/'
                        '6f7f8b99bdc7970c4cfa833f14798e0b.jpg'
                    ),
                    brand='Samsung',
                    reviewScore=4.8,
                ),
                Product(
                    title='Ar Condicionado Split Inverter '
                    'Hi Wall Springer Midea Xtreme Save '
                    'Connect Black Edition 18000 BTUs '
                    'Quente/Frio 42MGVQI18M5 - 220V',
                    price=5221.11,
                    image=(
                        'https://a-static.mlcdn.com.br/800x560/ar-condicionado-split-inverter-'
                        'hi-wall-springer-midea-xtreme-save-connect-black-edition-18000-btus-'
                        'quente-frio-42mgvqi18m5-220v/dufrio/100285446/5d0556dd1ff679fdcd5a167'
                        'acec5f65b.jpeg'
                    ),
                    brand='Midea',
                    reviewScore=5,
                ),
                Product(
                    title='Smartphone Samsung Galaxy '
                    'S23 Ultra 256GB Preto 5G 12GB RAM 6,8” '
                    'Câm. Quádrupla + Selfie 12MP',
                    price=4999.10,
                    image=(
                        'https://a-static.mlcdn.com.br/800x560/smartphone-samsung-galaxy-s23-'
                        'ultra-256gb-preto-5g-12gb-ram-68-cam-quadrupla-selfie-12mp/'
                        'magazineluiza/232855300/e339efd56b869f6a89daf54439feefda.jpg'
                    ),
                    brand='Samsung',
                    reviewScore=4.9,
                ),
                Product(
                    title='Smartband Samsung Galaxy Fit3 Grafite',
                    price=499,
                    image=(
                        'https://a-static.mlcdn.com.br/800x560/smartband-samsung-galaxy-fit3-'
                        'grafite/magazineluiza/237271000/1228c51df33a2aef493975b2f27e1273.jpg'
                    ),
                    brand='Samsung',
                    reviewScore=4.8,
                ),
                Product(
                    title='Purificador Electrolux Água Gelada'
                    'Fria e Natural com Painel Easy '
                    'Touch Cinza (PE11X)',
                    price=649,
                    image=(
                        'https://a-static.mlcdn.com.br/800x560/purificador-electrolux-agua-'
                        'gelada-fria-e-natural-com-painel-easy-touch-cinza-pe11x/electrolux/'
                        '2002605/b5604a0486939cde3a9dce07bda3e419.jpeg'
                    ),
                    brand='Electrolux',
                    reviewScore=4.4,
                ),
                Product(
                    title='Pneu Aro 13” 175/70R13 '
                    'Goodyear 82T Direction Touring 2',
                    price=336.74,
                    image=(
                        'https://a-static.mlcdn.com.br/800x560/pneu-aro-13-175-70r13-'
                        'goodyear-82t-direction-touring-2/magazineluiza/238099700/'
                        'd1c6353c1a1935f1d50ba0a9e78a8a6f.jpg'
                    ),
                    brand='Goodyear',
                    reviewScore=4.9,
                ),
                Product(
                    title='Manta Sofa Retratil 2,00x1,80 '
                    'Gigante Grande Xale Colcha Algodão - '
                    'SSCOMÉRCIO DE TAPETES',
                    price=4999.10,
                    image=(
                        'https://a-static.mlcdn.com.br/800x560/manta-sofa-retratil-200x180-'
                        'gigante-grande-xale-colcha-algodao-sscomercio-de-tapetes/'
                        'sscomerciodetapetes/d03c2e1c4c1711ee90084201ac185056/'
                        '5655764acf6e3733681d75b189c61c48.jpeg'
                    ),
                    brand='SSCOMÉRCIO DE TAPETES',
                    reviewScore=5,
                ),
                Product(
                    title='Tablet Positivo Vision Tab 10,1" '
                    '128GB 4GB RAM Android 13 Octa Core '
                    'Wi-Fi 4G',
                    price=999,
                    image=(
                        'https://a-static.mlcdn.com.br/800x560/tablet-positivo-vision-tab-'
                        '101-128gb-4gb-ram-android-13-octa-core-wi-fi-4g/magazineluiza/'
                        '238030600/6fe3b431b07ca5bb6939c59bf10f78c0.jpg'
                    ),
                    brand='Positivo',
                    reviewScore=4.6,
                ),
                Product(
                    title='Creatina Pura 100% Monohidratada '
                    '250g, Creatine Micronizada - '
                    'Denavita',
                    price=56.91,
                    image=(
                        'https://a-static.mlcdn.com.br/800x560/creatina-pura-100-monohidratada-'
                        '250g-creatine-micronizada-denavita/denavitta/creatina100puradenavita/'
                        '30b45b14474b5a16319c79efdc382c1c.jpeg'
                    ),
                    brand='DENAVITA',
                    reviewScore=4.5,
                ),
                Product(
                    title='Furadeira e Parafusadeira Wap'
                    'a Bateria 12V com Maleta 13 Peças BPF '
                    '12K3',
                    price=199.89,
                    image=(
                        'https://a-static.mlcdn.com.br/800x560/furadeira-e-parafusadeira-wap-a-'
                        'bateria-12v-com-maleta-13-pecas-bpf-12k3/magazineluiza/236188200/'
                        '0d28b847474998bb676b6023723b430b.jpg'
                    ),
                    brand='Wap',
                    reviewScore=4.8,
                ),
            ]

            session.add_all(products)
            session.commit()


if __name__ == '__main__':
    seed_products()
