from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Product, Review, FAQ, ContactMessage


class MarigoldAdminSite(AdminSite):
    site_header = 'Marigold & Co.'
    site_title  = 'Marigold Admin'
    index_title = 'Dashboard'

    def _get_extra_context(self):
        return {
            'product_count':      Product.objects.count(),
            'featured_count':     Product.objects.filter(is_featured=True, is_active=True).count(),
            'message_count':      ContactMessage.objects.count(),
            'unread_count':       ContactMessage.objects.filter(is_read=False).count(),
            'recent_messages':    ContactMessage.objects.order_by('-sent_at')[:5],
            'review_count':       Review.objects.count(),
            'pending_reviews':    Review.objects.filter(is_approved=False).count(),
            'unapproved_reviews': Review.objects.filter(is_approved=False).order_by('-created_at')[:3],
            'faq_count':          FAQ.objects.filter(is_active=True).count(),
        }

    def index(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context.update(self._get_extra_context())
        return super().index(request, extra_context)

    def app_index(self, request, app_label, extra_context=None):
        extra_context = extra_context or {}
        extra_context.update(self._get_extra_context())
        return super().app_index(request, app_label, extra_context)


marigold_admin = MarigoldAdminSite(name='admin')

# ── Register auth models ───────────────────────────────────────
marigold_admin.register(User, UserAdmin)


# ── Register app models ────────────────────────────────────────
@admin.register(ContactMessage, site=marigold_admin)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display    = ['first_name', 'last_name', 'email', 'subject', 'sent_at', 'is_read']
    list_filter     = ['subject', 'is_read']
    search_fields   = ['first_name', 'last_name', 'email']
    readonly_fields = ['first_name', 'last_name', 'email', 'subject', 'message', 'sent_at']
    list_editable   = ['is_read']


@admin.register(Product, site=marigold_admin)
class ProductAdmin(admin.ModelAdmin):
    list_display  = ['name', 'category', 'price', 'is_active', 'is_featured', 'created_at']
    list_filter   = ['category', 'is_active', 'is_featured']
    search_fields = ['name', 'category']
    list_editable = ['is_active', 'is_featured']


@admin.register(Review, site=marigold_admin)
class ReviewAdmin(admin.ModelAdmin):
    list_display  = ['author', 'location', 'rating', 'is_approved', 'created_at']
    list_filter   = ['is_approved', 'rating']
    list_editable = ['is_approved']


@admin.register(FAQ, site=marigold_admin)
class FAQAdmin(admin.ModelAdmin):
    list_display  = ['question', 'category', 'order', 'is_active']
    list_filter   = ['category', 'is_active']
    list_editable = ['order', 'is_active']