from django.shortcuts import render
from django.views.generic import TemplateView, View
# Create your views here.
from texts.models import SectionTitle,HeaderText, AboutCard, ServiceCard, ProcessCard, ContactInfo, FooterText
from images.models import HeaderImage, GalleryImage
from links.models import SocialMediaLink, MenuItem
from .mail_sender import send_contact_us_notification

class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Texts
        # Fetch section titles
        section_titles = {}
        for section in SectionTitle.objects.all():
            section_titles[section.section.replace("-","_")] = section.title
        context['section_titles'] = section_titles
        # Fetch header texts
        header_texts = {}
        for header in HeaderText.objects.all():
            header_texts[header.type.replace("-","_")] = header.content
        context['header_texts'] = header_texts
        # Fetch about cards
        context['about_cards'] = AboutCard.objects.all()
        # Fetch service cards
        context['service_cards'] = []
        for service in ServiceCard.objects.all():
            services_list = service.list_of_services.splitlines()
            context['service_cards'].append({
                'title': service.title,
                'subtitle': service.subtitle,
                'list_of_services': services_list
            })
        # Fetch process cards ordered by step_number
        context['process_cards'] = ProcessCard.objects.all().order_by('step_number')
        # Fetch contact info
        contact_info = {}
        for info in ContactInfo.objects.all():
            contact_info[info.type.replace("-","_")] = info.content
        context['contact_info'] = contact_info
        # Fetch footer texts
        footer_texts = {}
        for footer in FooterText.objects.all():
            footer_texts[footer.type.replace("-","_")] = footer.content
        context['footer_texts'] = footer_texts


        # Images
        # Fetch header images
        header_images = {}
        for img in HeaderImage.objects.all():
            header_images[img.type.replace("-","_")] = img.image.url
        context['header_images'] = header_images
        # Fetch gallery images
        context['gallery_images'] = GalleryImage.objects.all()

        # Social Media Links
        social_links = {}
        for link in SocialMediaLink.objects.all():
            social_links[link.platform.replace("-","_")] = link.url
        context['social_links'] = social_links

        # Menu Items
        context['menu_items'] = MenuItem.objects.all().order_by('order')

        return context

class SendContactUsInfoView(View):
    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Send email notification
        send_contact_us_notification(name, phone, email, message)

        return render(request, 'contact_us_submit.html', {'name': name})