import streamlit as st
import openai
import os

import pandas as pd


def app():

  st.title("Facebook Ad Headline genrator")
  st.markdown("###### Here you get to generate a Facebook ad headline")
  st.markdown(
    "###### 1) Simply Write your Input keyword in the empty field below")
  str = st.text_area("Keyword")
  promptff = f"\nKeyword: {str}.\nFacebook ad headline:"
  Analyzer_choice = st.selectbox("Select model", ["Curie", "Davinci"])
  button = st.button("Generate headline")
  if Analyzer_choice == "Curie":
    if button and promptff:
      user_input = promptff
      openai.api_key = "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"
      with st.spinner("Generating Headline, please wait.."):
        response = openai.Completion.create(
          model="text-curie-001",
          prompt=
          f"This is an AI bot that generates witty and sassy headlines for Facebook ads in the output by taking a keyword in the input.\nKeyword: Building amazing business.\nFacebook ad headline: \"The Ultimate Guide to Building a Business That Makes You Money and Makes a Difference\".\n#\nKeyword: Email marketing improvement.\nFacebook ad headline: \"Why Your Email Marketing Sucks (And How to Fix It in 5 Minutes)\".\n#\nKeyword: Content creation and sales boost.\nFacebook ad headline:\"How to Create Content That Connects with Your Audience and Boosts Your Sales\".\n#\nKeyword: Passive income generation.\nFacebook ad headline:\"The Secret to Making Money While You Sleep (Hint: It's Not a Get Rich Quick Scheme)\"\n#\nKeyword: Website optimization for customer conversion\nFacebook ad headline:\"Why Your Website Is Repelling Potential Customers (And What to Do About It)\"\n#\nKeyword: Online course launch for beginners.\nFacebook ad headline:\"The Ultimate Guide to Launching a Successful Online Course (Even If You're a Beginner)\"\n#\nKeyword: Instagram growth and algorithm optimization.\nFacebook ad headline:\"How to Master Instagram and Grow Your Following (Without Being a Slave to the Algorithm)\"\n#\nKeyword: Mindset for success cultivation.\nFacebook ad headline:\"Why Your Mindset is the Key to Your Success (And How to Cultivate a Winning Attitude)\"\n#\nKeyword: Confident sales approach.\nFacebook ad headline:\"The Art of Selling Without Feeling Sleazy: How to Close Deals with Confidence\"\n#\nKeyword: Podcast creation for audience engagement.\nFacebook ad headline:\"How to Create a Podcast That People Actually Want to Listen To (And Share)\"\n#\nKeyword: Overcoming fear and taking action.\nFacebook ad headline:\"Why You Should Stop Making Excuses and Start Taking Action (Even If You're Scared)\"\n#\nKeyword: Business outsourcing for better work-life balance.\nFacebook ad headline:\"The Ultimate Guide to Outsourcing Your Business (And Getting Your Life Back)\"\n#\nKeyword: Video marketing for lead and sales generation without camera presence.\nFacebook ad headline:\"How to Use Video Marketing to Attract More Leads and Sales (Without Being on Camera)\"\n#\nKeyword: Overcoming perfectionism for success.\nFacebook ad headline:\"Why Being a Perfectionist is Sabotaging Your Success (And What to Do Instead)\"\n#\nKeyword: Copywriting for high conversion rates.\nFacebook ad headline:\"The Art of Copywriting: How to Write Words That Sell (And Convert Like Crazy)\"\n#\nKeyword: Focusing on effective strategies over distractions.\nFacebook ad headline:\"Why You Should Stop Chasing Shiny Objects and Focus on What Works (And What Doesn't)\"\n#\nKeyword: Webinar hosting for conversion without camera presence.\nFacebook ad headline:\"The Ultimate Guide to Hosting Webinars That Convert (Even If You're Camera-Shy)\"\n#\nKeyword: Brand building for value alignment and ideal customer attraction.\nFacebook ad headline:\"How to Build a Brand That Reflects Your Values (And Attracts Your Ideal Customers)\"\n#\nKeyword: Embracing unique selling proposition for market differentiation.\nFacebook ad headline:\"Why You Should Embrace Your Unique Selling Proposition (And Stand Out in a Crowded Market)\"\n#\nKeyword: Community building for fan and superfan creation.\nFacebook ad headline:\"The Art of Building an Engaged Community: How to Create Fans and Superfans\"\n#\nKeyword: Avoiding boring branding.\nFacebook ad headline:\"Why being boring is the worst branding sin you can commit\"\n#\nKeyword: Seductive copywriting for customer attraction.\nFacebook ad headline:\"The art of seducing your customers (with words)\"\n#\nKeyword: Standing out from conventional professionalism.\nFacebook ad headline:\"Why being 'professional' is overrated (and how to stand out)\"\n#\nKeyword: Personality in branding for impact.\nFacebook ad headline:\"The power of personality in branding (and why you need it)\"\n#\nKeyword: Effective brand voice development.\nFacebook ad headline:\"How to make your brand voice sing (even if you're not a writer)\"\n#\nKeyword: Unconventional branding for memorability.\nFacebook ad headline:\"Why being weird is the key to memorable branding\"\n#\nKeyword: Creating brand loyalty.\nFacebook ad headline:\"The secret to making your customers fall in love with your brand\"\n#\nKeyword: Conversational copywriting for relationship building.\nFacebook ad headline:\"How to write copy that feels like a conversation (not a sales pitch)\"\n#\nKeyword: Authenticity in marketing.\nFacebook ad headline: \"Why authenticity is the new marketing buzzword (and how to be authentic)\"\n#\nKeyword: Branding mistake correction.\nFacebook ad headline: \"The one branding mistake you're making (and how to fix it)\"\n#{user_input}",
          temperature=0.9,
          max_tokens=100,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0)

      st.write(response['choices'][0]['text'])

  else:
    if button and promptff:
      user_input = promptff
      openai.api_key = "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"
      with st.spinner("Generating Headline, please wait.."):
        response2 = openai.Completion.create(
          model="text-davinci-003",
          prompt=
          f"This is an AI bot that generates witty and sassy headlines for Facebook ads in the output by taking a keyword in the input.\nKeyword: Building amazing business.\nFacebook ad headline: \"The Ultimate Guide to Building a Business That Makes You Money and Makes a Difference\".\n#\nKeyword: Email marketing improvement.\nFacebook ad headline: \"Why Your Email Marketing Sucks (And How to Fix It in 5 Minutes)\".\n#\nKeyword: Content creation and sales boost.\nFacebook ad headline:\"How to Create Content That Connects with Your Audience and Boosts Your Sales\".\n#\nKeyword: Passive income generation.\nFacebook ad headline:\"The Secret to Making Money While You Sleep (Hint: It's Not a Get Rich Quick Scheme)\"\n#\nKeyword: Website optimization for customer conversion\nFacebook ad headline:\"Why Your Website Is Repelling Potential Customers (And What to Do About It)\"\n#\nKeyword: Online course launch for beginners.\nFacebook ad headline:\"The Ultimate Guide to Launching a Successful Online Course (Even If You're a Beginner)\"\n#\nKeyword: Instagram growth and algorithm optimization.\nFacebook ad headline:\"How to Master Instagram and Grow Your Following (Without Being a Slave to the Algorithm)\"\n#\nKeyword: Mindset for success cultivation.\nFacebook ad headline:\"Why Your Mindset is the Key to Your Success (And How to Cultivate a Winning Attitude)\"\n#\nKeyword: Confident sales approach.\nFacebook ad headline:\"The Art of Selling Without Feeling Sleazy: How to Close Deals with Confidence\"\n#\nKeyword: Podcast creation for audience engagement.\nFacebook ad headline:\"How to Create a Podcast That People Actually Want to Listen To (And Share)\"\n#\nKeyword: Overcoming fear and taking action.\nFacebook ad headline:\"Why You Should Stop Making Excuses and Start Taking Action (Even If You're Scared)\"\n#\nKeyword: Business outsourcing for better work-life balance.\nFacebook ad headline:\"The Ultimate Guide to Outsourcing Your Business (And Getting Your Life Back)\"\n#\nKeyword: Video marketing for lead and sales generation without camera presence.\nFacebook ad headline:\"How to Use Video Marketing to Attract More Leads and Sales (Without Being on Camera)\"\n#\nKeyword: Overcoming perfectionism for success.\nFacebook ad headline:\"Why Being a Perfectionist is Sabotaging Your Success (And What to Do Instead)\"\n#\nKeyword: Copywriting for high conversion rates.\nFacebook ad headline:\"The Art of Copywriting: How to Write Words That Sell (And Convert Like Crazy)\"\n#\nKeyword: Focusing on effective strategies over distractions.\nFacebook ad headline:\"Why You Should Stop Chasing Shiny Objects and Focus on What Works (And What Doesn't)\"\n#\nKeyword: Webinar hosting for conversion without camera presence.\nFacebook ad headline:\"The Ultimate Guide to Hosting Webinars That Convert (Even If You're Camera-Shy)\"\n#\nKeyword: Brand building for value alignment and ideal customer attraction.\nFacebook ad headline:\"How to Build a Brand That Reflects Your Values (And Attracts Your Ideal Customers)\"\n#\nKeyword: Embracing unique selling proposition for market differentiation.\nFacebook ad headline:\"Why You Should Embrace Your Unique Selling Proposition (And Stand Out in a Crowded Market)\"\n#\nKeyword: Community building for fan and superfan creation.\nFacebook ad headline:\"The Art of Building an Engaged Community: How to Create Fans and Superfans\"\n#\nKeyword: Avoid boring branding.\nFacebook ad headline:\"Why being boring is the worst branding sin you can commit\"\n#\nKeyword: Seductive copywriting for customer attraction.\nFacebook ad headline:\"The art of seducing your customers (with words)\"\n#\nKeyword: Standing out from conventional professionalism.\nFacebook ad headline:\"Why being 'professional' is overrated (and how to stand out)\"\n#\nKeyword: Personality in branding for impact.\nFacebook ad headline:\"The power of personality in branding (and why you need it)\"\n#\nKeyword: Effective brand voice development.\nFacebook ad headline:\"How to make your brand voice sing (even if you're not a writer)\"\n#\nKeyword: Unconventional branding for memorability.\nFacebook ad headline:\"Why being weird is the key to memorable branding\"\n#\nKeyword: Creating brand loyalty.\nFacebook ad headline:\"The secret to making your customers fall in love with your brand\"\n#\nKeyword: Conversational copywriting for relationship building.\nFacebook ad headline:\"How to write copy that feels like a conversation (not a sales pitch)\"\n#\nKeyword: Authenticity in marketing.\nFacebook ad headline: \"Why authenticity is the new marketing buzzword (and how to be authentic)\"\n#\nKeyword: Branding mistake correction.\nFacebook ad headline: \"The one branding mistake you're making (and how to fix it)\"\n#{user_input}",
          temperature=0.9,
          max_tokens=100,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0)

      st.write(response2['choices'][0]['text'])


if __name__ == "__main__":
  app()
