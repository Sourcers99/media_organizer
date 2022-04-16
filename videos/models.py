from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from django.core.validators import FileExtensionValidator

from config import readConfig
data = readConfig()

# Create your models here.
class Staralias(models.Model):

    star_alias_name = models.CharField(_(""), max_length=50)

    class Meta:
        verbose_name = _("Staralias")
        verbose_name_plural = _("Staraliass")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Staralias_detail", kwargs={"pk": self.pk})


class Star(models.Model):
    GENDER = [
        ("Female", "Female"),
        ("Male", "Male"),
        ("Trans", "Trans")
    ]
    star_name = models.CharField(_("Star Name"), max_length=50)
    star_image = models.ImageField(_("Star Image"), upload_to=data["images-store-path"])
    star_alias = models.ManyToManyField("Staralias", verbose_name=_("Alias"))
    star_dob = models.CharField(_("Star DOB"), max_length=50)
    star_bio = models.TextField(_("Star Bio"))
    star_boob_size = models.CharField(_("Star Boob Size"), max_length=50)
    star_gender = models.CharField(_("Star Gender"), max_length=50, choices=GENDER, default="Female")

    class Meta:
        verbose_name = _("Star")
        verbose_name_plural = _("Stars")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Star_detail", kwargs={"pk": self.pk})

class Category(models.Model):
    category_name = models.CharField(_("Category Name"), max_length=50)
    category_image = models.ImageField(_("Category Image"), upload_to=data["images-store-path"])
    

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"pk": self.pk})

class Tag(models.Model):

    tag_name = models.CharField(_("Tag Name"), max_length=50)
    tag_image = models.ImageField(_("Tag Image"), upload_to=data["images-store-path"])

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Tag_detail", kwargs={"pk": self.pk})

class Subsite(models.Model):

    subsite_name = models.CharField(_("Subsite Name"), max_length=50)
    subsite_image = models.ImageField(_("Subsite Image"), upload_to=data["images-store-path"])
    subsite_url = models.URLField(_("Subsite URL"), max_length=200)    

    class Meta:
        verbose_name = _("subsite")
        verbose_name_plural = _("subsites")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("subsite_detail", kwargs={"pk": self.pk})


class Channel(models.Model):

    channel_name = models.CharField(_("Channel Name"), max_length=50)
    channel_image = models.ImageField(_("Channel Image"), upload_to=data["images-store-path"])
    channel_subsite = models.ManyToManyField("Subsite", verbose_name=_("Subsites"))
    channel_url = models.URLField(_("Channel URL"), max_length=200)

    class Meta:
        verbose_name = _("Channel")
        verbose_name_plural = _("Channels")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Channel_detail", kwargs={"pk": self.pk})

class Video(models.Model):

    video_name = models.CharField(_("Video Name"), max_length=50)
    video_image = models.ImageField(_("Video Image"), upload_to=data["images-store-path"])
    video_pub_date = models.DateField(_("Video Published"), auto_now=False, auto_now_add=False, blank=True, null=True)
    video_desc = models.TextField(_("Video Description"))
    video_stars = models.ManyToManyField("Star", verbose_name=_("Stars"))
    video_channel = models.ForeignKey("Channel", verbose_name=_("Channel"), on_delete=models.CASCADE, null=True, blank=True)
    video_path = models.CharField(_("Video Path"), max_length=50)
    video_tags = models.ManyToManyField("Tag", verbose_name=_("Video Tag"))
    video_category = models.ManyToManyField("Category", verbose_name=_("Video Category"))
    video_url = models.URLField(_("Video URL"), max_length=200)

    class Meta:
        verbose_name = _("Video")
        verbose_name_plural = _("Videos")

    def __str__(self):
        return self.video_name

    def get_absolute_url(self):
        return reverse("Video_detail", kwargs={"pk": self.pk})
