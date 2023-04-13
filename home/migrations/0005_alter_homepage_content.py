# Generated by Django 4.1.7 on 2023-04-13 20:33

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_homepage_search_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="homepage",
            name="content",
            field=wagtail.fields.StreamField(
                [
                    (
                        "hero",
                        wagtail.blocks.StructBlock(
                            [
                                ("image", wagtail.images.blocks.ImageChooserBlock()),
                                (
                                    "content",
                                    wagtail.blocks.StreamBlock(
                                        [
                                            (
                                                "heading",
                                                wagtail.blocks.StructBlock(
                                                    [
                                                        (
                                                            "heading",
                                                            wagtail.blocks.ChoiceBlock(
                                                                choices=[
                                                                    ("h1", "Heading 1"),
                                                                    ("h2", "Heading 2"),
                                                                    ("h3", "Heading 3"),
                                                                    ("h4", "Heading 4"),
                                                                ]
                                                            ),
                                                        ),
                                                        ("text", wagtail.blocks.TextBlock()),
                                                    ]
                                                ),
                                            )
                                        ]
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "contact_us",
                        wagtail.blocks.StructBlock(
                            [
                                ("heading", wagtail.blocks.TextBlock()),
                                ("sub_heading", wagtail.blocks.TextBlock()),
                                ("photo", wagtail.images.blocks.ImageChooserBlock(required=False)),
                                ("email", wagtail.blocks.EmailBlock()),
                                ("phone_number", wagtail.blocks.CharBlock(max_length=20)),
                            ]
                        ),
                    ),
                ],
                null=True,
                use_json_field=True,
            ),
        ),
    ]
