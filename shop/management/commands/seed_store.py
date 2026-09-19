from django.core.management.base import BaseCommand
from shop.models import Category, Product

CATEGORIES=[('Electronics','electronics','⌁'),('Fashion','fashion','✦'),('Home & Living','home-living','⌂'),('Beauty & Care','beauty-care','✧')]
PRODUCTS=[
('Wireless ANC Earbuds','wireless-anc-earbuds','Electronics','Immersive sound with active noise cancellation.','Premium everyday earbuds with low-latency mode and a pocket charging case.',6999,8999,25,'https://images.unsplash.com/photo-1606220945770-b5b6c2c55bf1?auto=format&fit=crop&w=900&q=80','BESTSELLER',True),
('Minimal Leather Wallet','minimal-leather-wallet','Fashion','Slim genuine-leather wallet for everyday carry.','A clean profile with practical card slots and a timeless finish.',2499,3299,40,'https://images.unsplash.com/photo-1627123424574-724758594e93?auto=format&fit=crop&w=900&q=80','NEW',True),
('Insulated Travel Tumbler','insulated-travel-tumbler','Home & Living','Keep tea, coffee or water at the right temperature.','Double-wall insulated stainless steel tumbler with a spill-resistant lid.',2999,3999,30,'https://images.unsplash.com/photo-1544145945-f90425340c7e?auto=format&fit=crop&w=900&q=80','TRENDING',True),
('Everyday Canvas Tote','everyday-canvas-tote','Fashion','Strong reusable tote for work, uni and errands.','Heavy canvas construction with a structured base and comfortable handles.',1899,None,50,'https://images.unsplash.com/photo-1590874103328-eac38a683ce7?auto=format&fit=crop&w=900&q=80','',False),
('Desk Lamp Pro','desk-lamp-pro','Home & Living','Warm adjustable light for focused work.','Minimal desk lamp with three brightness levels and a weighted metal base.',4499,5499,18,'https://images.unsplash.com/photo-1507473885765-e6ed057f782c?auto=format&fit=crop&w=900&q=80','',True),
('Daily Face Cleanser','daily-face-cleanser','Beauty & Care','Gentle daily cleanser for a fresh, clean finish.','A simple, non-stripping cleanser for morning and evening routines.',1599,1999,45,'https://images.unsplash.com/photo-1556229010-6c3f2c9ca5f8?auto=format&fit=crop&w=900&q=80','',False),
('Everyday Backpack','everyday-backpack','Fashion','Clean commuter backpack with laptop sleeve.','Water-resistant fabric, padded laptop compartment and smart internal storage.',5499,6999,20,'https://images.unsplash.com/photo-1553062407-98eeb64c6a62?auto=format&fit=crop&w=900&q=80','POPULAR',True),
('Smart LED Strip','smart-led-strip','Electronics','Ambient lighting for bedrooms and workspaces.','App-ready RGB strip with scene modes and music sync.',2199,2799,35,'https://images.unsplash.com/photo-1550745165-9bc0b252726f?auto=format&fit=crop&w=900&q=80','',False),
]
class Command(BaseCommand):
    help='Load polished demo categories and products.'
    def handle(self,*args,**kwargs):
        cats={}
        for name,slug,icon in CATEGORIES:
            c,_=Category.objects.update_or_create(slug=slug,defaults={'name':name,'icon':icon}); cats[name]=c
        for data in PRODUCTS:
            name,slug,cat,short,desc,price,old,stock,img,badge,featured=data
            Product.objects.update_or_create(slug=slug,defaults={'name':name,'category':cats[cat],'short_description':short,'description':desc,'price':price,'old_price':old,'stock':stock,'image_url':img,'badge':badge,'featured':featured,'active':True})
        self.stdout.write(self.style.SUCCESS('BazaarPK demo store seeded successfully.'))
