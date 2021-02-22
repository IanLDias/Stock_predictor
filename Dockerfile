FROM wajdikh/fbprophet

EXPOSE 8501
WORKDIR /streamlit-docker
COPY requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt

COPY . .
CMD streamlit run main.py

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
RUN mkdir -p /root/.streamlit
RUN bash -c 'echo -e "\
[general]\n\
email = \"\"\n\
" > /root/.streamlit/credentials.toml'

RUN bash -c 'echo -e "\
[server]\n\
enableCORS = false\n\
" > /root/.streamlit/config.toml'