# Pop3D

**Qualquer filme em 3D de verdade, no seu óculos VR.**

<p align="center"><img src="docs/img/parallax.gif" width="560" alt="Foto de um lago separada em camadas de profundidade, se movendo como em 3D"></p>

O Pop3D usa inteligência artificial para transformar filmes, séries e vídeos 2D em 3D, na hora, direto no seu Meta Quest ou óculos de PC. Sem converter nada, sem configurar nada. Grátis.

### [Baixar o Pop3D para Windows](https://github.com/Sindelitcis/pop3d/releases/latest)

Site: **https://pop3d.quest**

## O que ele faz

- **100% automático:** descobre sua placa de vídeo, escolhe a melhor qualidade e encontra seu óculos sozinho.
- **Seus filmes em 3D:** filmes e séries 2D viram 3D enquanto você assiste. Filmes 3D também tocam direto.
- **A tela do PC em 3D:** YouTube, streaming e jogos aparecem em 3D no óculos.
- **Sem fio no Quest:** com o app Pop3D no Meta Quest, o filme chega pelo Wi-Fi.

## Como funciona

1. Para cada quadro do vídeo, um modelo de IA estima a distância de cada ponto até a câmera.
2. Com essa profundidade, a imagem é separada em planos, do mais perto ao mais longe.
3. O que estava escondido atrás dos objetos da frente é reconstruído, para não sobrar buraco quando a cena muda de ângulo.
4. Saem duas imagens um pouco diferentes, uma para cada olho, e o óculos mostra como 3D.

Tudo roda na placa de vídeo do seu PC, enquanto o filme passa. A profundidade vem do
[Video Depth Anything](https://github.com/DepthAnything/Video-Depth-Anything) através do
[iw3](https://github.com/nagadomi/nunif), em PyTorch com CUDA. No Meta Quest, o PC manda as imagens pelo
Wi-Fi para o [app do Quest](https://github.com/Sindelitcis/pop3d-quest), que é open source (GPLv3).

## Requisitos

| | |
|---|---|
| Sistema | Windows 10 ou 11 (64 bits) |
| Placa de vídeo | NVIDIA GeForce RTX (série 20 ou mais nova) |
| Espaço livre | 15 GB |
| Óculos | Meta Quest 2, 3 ou 3S, ou qualquer óculos de PC (SteamVR/OpenXR) |

## Instalação

1. Baixe o `Pop3D_Instalador.exe` da [versão mais nova](https://github.com/Sindelitcis/pop3d/releases/latest).
2. Abra e clique em Avançar. Na primeira vez ele baixa uns 4 GB e prepara a IA para a sua placa de vídeo.
3. Pronto. Depois disso o Pop3D se atualiza sozinho.

> Se o Windows mostrar "O Windows protegeu o seu computador", clique em **Mais informações** e depois em **Executar assim mesmo**. Isso aparece com programas novos que a Microsoft ainda não conhece.

## Privacidade

Seus filmes nunca saem do seu computador. O app envia apenas estatísticas anônimas de uso (placa de vídeo, desempenho, erros), e isso pode ser desligado nos Ajustes. Detalhes na [Política de Privacidade](https://pop3d.quest/privacidade.html).

## Achou um problema?

[Conta pra gente](https://github.com/Sindelitcis/pop3d/issues): o que aconteceu, o modelo da sua placa de vídeo e do seu óculos.

## Este repositório

Aqui ficam o site (`docs/`, publicado em pop3d.quest) e os scripts que o geram (`site/`), além dos
instaladores em [Releases](https://github.com/Sindelitcis/pop3d/releases). O código do app do Quest está em
[pop3d-quest](https://github.com/Sindelitcis/pop3d-quest).

## English

**Pop3D** is a free Windows app that turns 2D movies, shows and videos into 3D while they play,
and shows them in a VR headset.

- An AI model estimates depth for every frame. The image is split into layers, the parts hidden
  behind foreground objects are filled in, and one view is rendered for each eye.
- It runs on your NVIDIA graphics card. Depth comes from Video Depth Anything through iw3, on PyTorch with CUDA.
- Meta Quest 2, 3 and 3S receive the picture over Wi-Fi through the
  [Quest app](https://github.com/Sindelitcis/pop3d-quest) (open source, GPLv3). PC headsets work through SteamVR or OpenXR.
- Your videos never leave your computer. The app sends anonymous usage statistics (graphics card,
  performance, errors), which you can turn off in Settings.

**Requirements:** Windows 10 or 11 (64-bit), NVIDIA GeForce RTX 20 series or newer, 15 GB free.

**Download:** [latest release](https://github.com/Sindelitcis/pop3d/releases/latest) · **Website:** https://pop3d.quest
