import React from 'react';
import './App.css';
import Header from './Header';
import Favorites from './Favorites';
import LyricsForm from './LyricsForm';
import LyricsLoading from './LyricsLoading';
import LyricsError from './LyricsError';
import LyricsResult from './LyricsResult';

export default class App extends React.Component {
  constructor(props) {
    super(props)

    this.state = {
      loading: false,
      error: false,
      artist: '',
      song: '',
      lyrics: null,
      favorites: [],
    }
  }
  loadLyrics(artist, song) {
    this.setState({
      artist,
      song,
      loading: true,
      error: false,
      lyrics: null,
    })

    fetch('https://api.lyrics.ovh/v1/' + artist + '/' + song)
      .then(response => response.json())
      .then(data => {
        this.setState({
          loading: false,
          error: Boolean(data.error),
          lyrics: data.lyrics,
        })
      })
  }
  addFavorite(artist, song) {
    fetch('http://localhost:8080/favorites', {
      method: 'post',
      body: JSON.stringify({artist, song})
    }).then(() => {
      this.loadFavorites()
    })
  }
  loadFavorites() {
    fetch('http://localhost:8080/favorites')
      .then(response => response.json())
      .then(({favorites}) => this.setState({favorites}));
  }
  render() {
    const {loading, error, artist, song, lyrics, favorites} = this.state

    return (
      <div>
        <Header />
        <div className="content">
          <div className="column-left dark">
            <Favorites
              favorites={favorites}
              loadFavorites={() => this.loadFavorites()}
              loadLyrics={(artist, song) => this.loadLyrics(artist, song)} />
          </div>
          <div className="column-right">
            <LyricsForm
              artist={artist}
              song={song}
              onSubmit={(artist, song) => this.loadLyrics(artist, song)} />
            <LyricsLoading loading={loading} />
            <LyricsError error={error} />
            <LyricsResult
              artist={artist}
              song={song}
              lyrics={lyrics}
              addFavorite={(artist, song) => this.addFavorite(artist, song)} />
          </div>
        </div>
      </div>
    );
  }
}
